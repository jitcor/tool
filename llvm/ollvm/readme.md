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

```
# 使用

## 问题
- Could NOT find OCaml
> 暂时没看出什么影响
# 参考
- https://www.cnblogs.com/theseventhson/p/14861940.html
- https://bbs.pediy.com/thread-217727.htm
- https://www.anquanke.com/post/id/86384
- https://www.bilibili.com/read/cv13148974


