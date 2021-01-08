# sqlcipher 3.x
64000,1024,sha1
# PRAGMA类参数解析核心函数
sqlcipher_codec_pragma:https://github.com/sqlcipher/sqlcipher/blob/master/src/crypto.c#L89
# PRAGMA key/rekey解析位置
# 注意事项
# iOS明文头问题
- sqlcipher 专门为iOS适配增加了一个设置选项cipher_plaintext_header_size，该选项可以让开头几个字节不参与加密
- 在这里面有个需要注意的地方，就是PRAGMA key的设置一定要放在PRAGMA cipher_plaintext_header_size前，以下举个例子
```
PRAGMA key = 'test';
PRAGMA cipher_plaintext_header_size = 32;
PRAGMA cipher_salt = "x'01010101010101010101010101010101'";
```
