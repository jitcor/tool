# LDR
![image](https://user-images.githubusercontent.com/27600008/147175743-a24f4d80-e8fb-48fe-9441-496b44fbbe55.png)
-参考:https://www.jianshu.com/p/66d801c85ee9
# LDUR
![image](https://user-images.githubusercontent.com/27600008/147073366-aa01d16d-b535-4cee-a3b5-5cb1de5308fe.png)
# STR
![image](https://user-images.githubusercontent.com/27600008/147075614-18ace765-7dcd-475e-b9ae-f372c49b6205.png)
> 存储时是按q0的类型存储的，q0是16字节，就要存储16字节
# EXTR
![image](https://user-images.githubusercontent.com/27600008/147079952-347d4893-b9e8-440e-8391-90a127e2049d.png)
- 等同于ROR，举例:`EXTR            W5, W21, W21, #0x17`->`ror w5, w21, #0x17`
# NEG
![image](https://user-images.githubusercontent.com/27600008/147091925-7048398d-ee0f-48a1-98ee-f37b4932f2e6.png)
- 简单理解就是加个负号，举例:`NEG w23,w3`->`w23=-w3`
# BIC
![image](https://user-images.githubusercontent.com/27600008/147094426-39cc8d25-c26c-4e55-8aff-237d2d1427d3.png)
- 举例:`bic     r0, r0, #6`->`r0=r0&(~6)`
# 条件代码
![image](https://user-images.githubusercontent.com/27600008/147219028-84581a82-061a-4c72-b194-8531bb18d6b2.png)
## BCC
![image](https://user-images.githubusercontent.com/27600008/147230427-9f9b16c3-8851-428c-8c48-e6d58204b12e.png)

# S
![image](https://user-images.githubusercontent.com/27600008/147220615-a9844314-cb86-45a2-a00b-412c43ecf8a1.png)
# NZCV
![image](https://user-images.githubusercontent.com/27600008/147321151-a2fe2f6c-3b67-492e-b9b3-f01d25fe9ea7.png)

# 未解决问题
- 1.将下图v5数组放入下面函数中，就会出现段错误，具体原因待研究
![image](https://user-images.githubusercontent.com/27600008/147350752-d335274b-26d5-4a75-a8b4-c4e8de427fe9.png)


# 参考
- http://www.lujun.org.cn/?p=1676
