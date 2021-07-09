# 简介
# 下载编译
- 环境：Window10 WSL
- 下载编译步骤
```
git clone https://github.com/llvm/llvm-project.git
cd llvm-project
mkdir build
cd build
cmake ../llvm
cmake --build .
```
- 编译成功后返回如下
- ![image](https://user-images.githubusercontent.com/27600008/125034648-67398700-e0c3-11eb-9c1c-054dcce1c0d9.png)
- 输出的二进制文件在build/bin目录下
- ![image](https://user-images.githubusercontent.com/27600008/125035041-e5962900-e0c3-11eb-9914-a2b63af81a03.png)


# 参考
- https://llvm.org/docs/GettingStarted.html
- https://github.com/llvm/llvm-project
