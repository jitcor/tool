# 简介
ARM相关
# 指令解析
```asm
EOR.W           R3, R3, R3,LSR#6 
```
对应c伪代码
```c
r3=r3^(r3>>6)
```
