# IDAPython
参考:[idapython](./../plugins/IDAPython/)
# get_bytes
> 从当前分析的二进制文件中dump出指定地址的数据 

![image](https://user-images.githubusercontent.com/27600008/153832313-c21b6363-4a44-4709-9978-48df342ead0c.png)
```python
get_bytes(0x1c004,16).hex()
```
- 参考:https://hex-rays.com/products/ida/support/idadoc/1600.shtml
# 寄存器操作
```python
idc.get_reg_value("r0")
idc.set_reg_value(0x80001,"r0")
```
# 内存操作
```
ida_bytes.get_dword(0xe2d88c60)->uint32
```
