# 通过秘钥获取原始秘钥
```python
import hashlib

print(hashlib.pbkdf2_hmac('sha1', bytes.fromhex('7f16632e1624672a12201123422f1b6d0c6d0061'),
                          bytes.fromhex('4DF4085B8FA8549CC2CF4E27C30A3EB8'), 64000, 32).hex())
```
