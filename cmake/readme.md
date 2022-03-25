# 安装
由于通过apt安装的版本很老，所以这里直接下载压缩包进行安装

压缩包下载地址https://cmake.org/files/

这里以WSL安装为例
```
export http_proxy=http://127.0.0.1:10809
export https_proxy=http://127.0.0.1:10809
wget https://cmake.org/files/v3.16/cmake-3.16.9-Linux-x86_64.tar.gz
tar -zxvf cmake-3.16.9-Linux-x86_64.tar.gz
cp -r ./cmake-3.16.9-Linux-x86_64 /usr/local/cmake
....
...
.
sudo ln -s /usr/local/cmake/bin/cmake /usr/bin/cmake
vim ~/.bashrc 
// 添加
export PATH=/usr/local/cmake/bin:$PATH
//esc
:wq
source ~/.bashrc
//check
cmake -version

```
# C语言项目
## 最简写法
```cmake
cmake_minimum_required(VERSION 3.16.3)
project(demo001 C)

set(CMAKE_C_STANDARD 99)
add_executable(demo001 main.c)
```
## 导入第三方库
## 打印详细输出信息
- 1.cmake命令行：`-DCMAKE_VERBOSE_MAKEFILE=ON`
- 2.cmakeLists.txt: `set(CMAKE_VERBOSE_MAKEFILEON ON)`
> 打印详细信息可以获取原始的g++编译命令行信息
