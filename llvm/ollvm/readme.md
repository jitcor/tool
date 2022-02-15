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
```
git clone -b llvm-4.0 --depth=1 https://github.com/obfuscator-llvm/obfuscator.git
cd obfuscator
mkdir build
cd build
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release -DLLVM_INCLUDE_TESTS=OFF ../
# 这里使用msys的make命令，所以在系统环境变量里一定要配置好msys的路径，我这里的路径就是D:\Linux-Program-Files\msys2\usr\bin
make -j7
```
# 使用

## 问题
- Could NOT find OCaml
> 暂时没看出什么影响
- Makefile:154: recipe for target 'all' failed
> 
# 参考
- https://www.cnblogs.com/theseventhson/p/14861940.html
- https://bbs.pediy.com/thread-217727.htm
- https://www.anquanke.com/post/id/86384
- https://www.bilibili.com/read/cv13148974


