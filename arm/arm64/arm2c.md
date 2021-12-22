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
- 举例:`NEG w23,w3`->`w23=-w3`
