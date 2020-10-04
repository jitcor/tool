# 通过秘钥获取原始秘钥
```python
import hashlib

print(hashlib.pbkdf2_hmac('sha1',b'password',b'salt', 64000, 32).hex())
```
- salt就是加密数据库前16个字节
- 64000 就是kdf次数
- 32 输出秘钥长度(固定)
