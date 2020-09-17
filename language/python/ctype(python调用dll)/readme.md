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
# 从参数读取返回值[<sup>1</sup>](#ref1)
```python
i = c_int()
c_func(byref(i))
print(i.value)
```
# 参考
- 1.[传递指针(或者传递引用)](https://docs.python.org/zh-cn/3/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference)<a id="ref1"/>
