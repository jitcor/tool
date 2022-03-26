# clion+ubuntu远程开发 
- ubuntu里配置好ssh服务(非root用户)
- clion Toolchains里添加该ssh工具链
- clion CMake里添加新的配置，并将toolchain指向该ssh工具链
- 然后用该CMake配置编译工程即可
> 前提ubuntu里已配置好相关编译环境：cmake,clang,gdb
