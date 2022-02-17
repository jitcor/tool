# 简介
# 编译
## WSL编译
```
git clone -b llvm-4.0 --depth=1 https://github.com/obfuscator-llvm/obfuscator.git
cd obfuscator
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF ../
make -j7
```
## Window编译
# 预编译
这里为排除系统环境变量干扰，需要先清洗下\
执行如下命令，重新设置PATH
```
set PATH=%DEF_PATH%;F:\tool\mingw\x86_64-8.1.0-release-posix-seh-rt_v6-rev0\mingw64\bin;H:\Program Files\CMake\bin\;
```
> DEF_PATH即系统默认的配置，具体参考https://github.com/Humenger/tool/blob/master/window/cmd.md \
> 另外自然是mingw和cmake配置了\
> MinGW下载地址https://github.com/Humenger/tool/releases/tag/MinGW

然后在当前窗口中执行如下命令\
```
git clone -b llvm-4.0 --depth=1 https://github.com/obfuscator-llvm/obfuscator.git
cd obfuscator
mkdir build
cd build
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF ../
mingw32-make -j16
```
最后编译结果 \
![image](https://user-images.githubusercontent.com/27600008/154421924-36523e23-8baa-4750-8339-f5ffcc8263e7.png)\
![image](https://user-images.githubusercontent.com/27600008/154422258-e1d2380b-a423-4bda-84cc-b94b3846c146.png)

> 虽然没有构建完成，但关键的clang.exe,clang++.exe,clang-format.exe都已经构建出来了
# 使用

## 问题
- Could NOT find OCaml
> 暂时没看出什么影响
- Makefile:154: recipe for target 'all' failed
> 可以忽略，只要关键文件都构建出来即可
# 参考
- https://www.cnblogs.com/theseventhson/p/14861940.html
- https://bbs.pediy.com/thread-217727.htm
- https://www.anquanke.com/post/id/86384
- https://www.bilibili.com/read/cv13148974


