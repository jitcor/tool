# 简介
ARM相关，以下所有汇编皆基于armv7
# 指令解析
```asm
EOR.W           R3, R3, R3,LSR#6 
```
对应c伪代码
```c
r3=r3^(r3>>6)
```
```asm
str     r3, [r2, r1, lsl #2] 
ldr     r3, [r2, r1, lsl #2] 
```

对应c伪代码

```c
r2[r1]=r3;//r2为32位整型数组
r3=r2[r1];
```
> 这里的汇编会有<<2操作，是因为整形占4字节，<<2也就是\*4,c里面的索引是按整形来数的，而汇编里是按字节来数的，所以需要\*4
# 指令分段
c里面各种语句可以分为几大类：变量定义，赋值，函数调用，所以可以在汇编找ldr,str,b等指令，根据这些指令进行分段，每段相当于c里一条语句
# 求余运算
汇编里的求余运算根据数值不同，五花八门，比如下面这个例子：

![7811696bf0de4acafdf978731712af6](https://user-images.githubusercontent.com/27600008/137833812-2cdf392d-6d94-49dd-b0e4-f2df3243ed1f.png)

# 指令优化
gcc在进行编译时，会进行各种复杂的优化，以提升执行效率，具体各种优化请参考：[Here](https://blog.csdn.net/qq_31108501/article/details/51842166)
- 函数内联

![image](https://user-images.githubusercontent.com/27600008/137844791-411867f0-108c-48d7-97d4-32afdc88fb6a.png)

- 指令段交叉

最后一步str赋值会穿插到下一段指令中

![image](https://user-images.githubusercontent.com/27600008/137893756-a7fc1a81-d771-4ef2-adca-2a2579d9d43e.png)


- 循环展开
# LDM与STM
详细参考：[Here](https://blog.csdn.net/petib_wangwei/article/details/41318395)

# 其他指令
- UXTB 参考：[HERE](https://blog.csdn.net/qq_26914291/article/details/120844547)
# 辅助工具
- 代码即时编译工具：https://godbolt.org/

![image](https://user-images.githubusercontent.com/27600008/137894473-577d60c5-c3eb-4aaa-a8ed-2d30e8778920.png)


- 代码即时运行调试工具：https://github.com/linouxis9/ARMStrong

![image](https://user-images.githubusercontent.com/27600008/137894522-252199b2-a65e-42b3-8aa4-2312c53fb5e2.png)

