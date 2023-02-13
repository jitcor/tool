## x密钥生成逻辑
```java
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
