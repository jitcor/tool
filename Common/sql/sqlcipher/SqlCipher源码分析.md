## x密钥生成逻辑
```c
/**
  * Set the keyspec for the cipher_ctx
  * 
  * returns SQLITE_OK if assignment was successfull
  * returns SQLITE_NOMEM if an error occured allocating memory
  */
static int sqlcipher_cipher_ctx_set_keyspec(cipher_ctx *ctx, const unsigned char *key, int key_sz, const unsigned char *salt, int salt_sz) {

    /* free, zero existing pointers and size */
  sqlcipher_free(ctx->keyspec, ctx->keyspec_sz);
  ctx->keyspec = NULL;
  ctx->keyspec_sz = 0;

  /* establic a hex-formated key specification, containing the raw encryption key and
     the salt used to generate it */
  ctx->keyspec_sz = ((key_sz + salt_sz) * 2) + 3;
  ctx->keyspec = sqlcipher_malloc(ctx->keyspec_sz);
  if(ctx->keyspec == NULL) return SQLITE_NOMEM;

  ctx->keyspec[0] = 'x';
  ctx->keyspec[1] = '\'';
  cipher_bin2hex(key, key_sz, ctx->keyspec + 2);
  cipher_bin2hex(salt, salt_sz, ctx->keyspec + (key_sz * 2) + 2);
  ctx->keyspec[ctx->keyspec_sz - 1] = '\'';
  return SQLITE_OK;
}
```
# x密钥解析逻辑
```c
/**
  * Derive an encryption key for a cipher contex key based on the raw password.
  *
  * If the raw key data is formated as x'hex' and there are exactly enough hex chars to fill
  * the key (i.e 64 hex chars for a 256 bit key) then the key data will be used directly. 

  * Else, if the raw key data is formated as x'hex' and there are exactly enough hex chars to fill
  * the key and the salt (i.e 92 hex chars for a 256 bit key and 16 byte salt) then it will be unpacked
  * as the key followed by the salt.
  * 
  * Otherwise, a key data will be derived using PBKDF2
  * 
  * returns SQLITE_OK if initialization was successful
  * returns SQLITE_ERROR if the key could't be derived (for instance if pass is NULL or pass_sz is 0)
  */
static int sqlcipher_cipher_ctx_key_derive(codec_ctx *ctx, cipher_ctx *c_ctx) {
  int rc;
  CODEC_TRACE("cipher_ctx_key_derive: entered c_ctx->pass=%s, c_ctx->pass_sz=%d \
                ctx->kdf_salt=%p ctx->kdf_salt_sz=%d c_ctx->kdf_iter=%d \
                ctx->hmac_kdf_salt=%p, c_ctx->fast_kdf_iter=%d c_ctx->key_sz=%d\n", 
                c_ctx->pass, c_ctx->pass_sz, ctx->kdf_salt, ctx->kdf_salt_sz, c_ctx->kdf_iter, 
                ctx->hmac_kdf_salt, c_ctx->fast_kdf_iter, c_ctx->key_sz); 
                
  
  if(c_ctx->pass && c_ctx->pass_sz) { // if pass is not null

    if(ctx->need_kdf_salt) {
      if(ctx->read_ctx->provider->random(ctx->read_ctx->provider_ctx, ctx->kdf_salt, FILE_HEADER_SZ) != SQLITE_OK) return SQLITE_ERROR;
      ctx->need_kdf_salt = 0;
    }
    if (c_ctx->pass_sz == ((c_ctx->key_sz * 2) + 3) && sqlite3StrNICmp((const char *)c_ctx->pass ,"x'", 2) == 0 && cipher_isHex(c_ctx->pass + 2, c_ctx->key_sz * 2)) { 
      int n = c_ctx->pass_sz - 3; /* adjust for leading x' and tailing ' */
      const unsigned char *z = c_ctx->pass + 2; /* adjust lead offset of x' */
      CODEC_TRACE("cipher_ctx_key_derive: using raw key from hex\n");
      cipher_hex2bin(z, n, c_ctx->key);
    } else if (c_ctx->pass_sz == (((c_ctx->key_sz + ctx->kdf_salt_sz) * 2) + 3) && sqlite3StrNICmp((const char *)c_ctx->pass ,"x'", 2) == 0 && cipher_isHex(c_ctx->pass + 2, (c_ctx->key_sz + ctx->kdf_salt_sz) * 2)) { 
      const unsigned char *z = c_ctx->pass + 2; /* adjust lead offset of x' */
      CODEC_TRACE("cipher_ctx_key_derive: using raw key from hex\n"); 
      cipher_hex2bin(z, (c_ctx->key_sz * 2), c_ctx->key);
      cipher_hex2bin(z + (c_ctx->key_sz * 2), (ctx->kdf_salt_sz * 2), ctx->kdf_salt);
    } else { 
      CODEC_TRACE("cipher_ctx_key_derive: deriving key using full PBKDF2 with %d iterations\n", c_ctx->kdf_iter); 
      c_ctx->provider->kdf(c_ctx->provider_ctx, c_ctx->pass, c_ctx->pass_sz, 
                    ctx->kdf_salt, ctx->kdf_salt_sz, c_ctx->kdf_iter,
                    c_ctx->key_sz, c_ctx->key);
    }

    /* set the context "keyspec" containing the hex-formatted key and salt to be used when attaching databases */
    if((rc = sqlcipher_cipher_ctx_set_keyspec(c_ctx, c_ctx->key, c_ctx->key_sz, ctx->kdf_salt, ctx->kdf_salt_sz)) != SQLITE_OK) return rc;

    /* if this context is setup to use hmac checks, generate a seperate and different 
       key for HMAC. In this case, we use the output of the previous KDF as the input to 
       this KDF run. This ensures a distinct but predictable HMAC key. */
    if(c_ctx->flags & CIPHER_FLAG_HMAC) {
      int i;

      /* start by copying the kdf key into the hmac salt slot
         then XOR it with the fixed hmac salt defined at compile time
         this ensures that the salt passed in to derive the hmac key, while 
         easy to derive and publically known, is not the same as the salt used 
         to generate the encryption key */ 
      memcpy(ctx->hmac_kdf_salt, ctx->kdf_salt, ctx->kdf_salt_sz);
      for(i = 0; i < ctx->kdf_salt_sz; i++) {
        ctx->hmac_kdf_salt[i] ^= hmac_salt_mask;
      } 

      CODEC_TRACE("cipher_ctx_key_derive: deriving hmac key from encryption key using PBKDF2 with %d iterations\n", 
        c_ctx->fast_kdf_iter); 

      
      c_ctx->provider->kdf(c_ctx->provider_ctx, c_ctx->key, c_ctx->key_sz, 
                    ctx->hmac_kdf_salt, ctx->kdf_salt_sz, c_ctx->fast_kdf_iter,
                    c_ctx->key_sz, c_ctx->hmac_key); 
    }

    c_ctx->derive_key = 0;
    return SQLITE_OK;
  };
  return SQLITE_ERROR;
}
```
> 可以看到若是密钥是x'----'格式，则不进行kdf计算，直接复制到最终aes的key上  
> salt 既用于kdf计算，也用于hmac计算  
