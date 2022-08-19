# 历史版本
https://cmake.org/files/
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
rm -rf /usr/bin/cmake
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
project(demo001)

set(CMAKE_C_STANDARD 99)
add_executable(demo001 main.c)
```
# 静态库
## 精简写法
```
cmake_minimum_required(VERSION 3.16.3)
project(demo002)
add_library(demo002 STATIC xx.c xxx.cc)
```
# 动态库
## 精简写法
```
cmake_minimum_required(VERSION 3.16.3)
project(demo002)
add_library(demo002 SHARE xx.c xxx.cc)
```

# 常用Api
```
# 设置输出目录
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY /path/to/out/dir/)
# 打印消息
message(STATUS "hello")
```
# 常用命令行Options
```
# 指定什么项目工程文件
-G "Unix Makefiles"
```
## 导入第三方库
## 打印详细输出信息
- 1.cmake命令行：`-DCMAKE_VERBOSE_MAKEFILE=ON`
- 2.cmakeLists.txt: `set(CMAKE_VERBOSE_MAKEFILEON ON)`
> 打印详细信息可以获取原始的g++编译命令行信息
# 小知识点
- vscode 里的cmake辅助插件，可以自动帮你列出当前系统已有的编译环境，然后让你选择  
