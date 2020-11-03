# 如何查看函数传入参数
- 在函数执行前断下，esp指向栈顶，也就是第一个参数,然后依次往下对应各个参数
```
00ECEE10   00ECEF48 //esp,arg0
00ECEE14   00ECEF5C //arg1
00ECEE18   0D4C2398 //arg2
00ECEE1C   00ECEF58 //...
...
00ECEE20   00ECEFC4 //...
00ECEE24   7D1783A3 //argn

```
