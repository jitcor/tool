# 模板
```python
ali = CDLL('ali.dll')
ali_aes_decrypt_key128 = ali.ali_aes_decrypt_key128
ali_aes_decrypt_key128.argtypes = [c_char_p, POINTER(c_uint)]
ali_aes_decrypt_key128.restype = None
ali_aes_decrypt = ali.ali_aes_decrypt
ali_aes_decrypt.argtypes = [c_char_p, POINTER(c_uint),POINTER(c_uint)]
ali_aes_decrypt.restype = c_int
```
# 传入参数
# 从参数读取返回值
