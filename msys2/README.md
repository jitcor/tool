# 下载安装
https://www.msys2.org/
# 安装python的Crypto库
```
pacman -S mingw-w64-x86_64-python-pycryptodome
```
# msys2软件包仓库
https://packages.msys2.org/queue
# pacman 使用
### 降级(安装指定版本)
##### 本地
```
Lenovo@DESKTOP-5MT4KVP MSYS ~
$ ls /var/cache/pacman/pkg
bash-4.4.023-2-x86_64.pkg.tar.xz
bash-completion-2.10-1-any.pkg.tar.xz
binutils-2.34-2-x86_64.pkg.tar.xz
brotli-1.0.7-3-x86_64.pkg.tar.xz
bsdcpio-3.4.2-2-x86_64.pkg.tar.xz
bsdtar-3.4.2-2-x86_64.pkg.tar.xz
bzip2-1.0.8-2-x86_64.pkg.tar.xz
ca-certificates-20190110-1-any.pkg.tar.xz
coreutils-8.32-1-x86_64.pkg.tar.xz
curl-7.69.1-1-x86_64.pkg.tar.xz
curl-7.70.0-1-x86_64.pkg.tar.zst
```
```
Lenovo@DESKTOP-5MT4KVP MSYS ~
$ pacman -U /var/cache/pacman/pkg/curl-7.70.0-1-x86_64.pkg.tar.zst
正在加载软件包...
警告：curl-7.70.0-1 已经为最新 -- 重新安装
正在解析依赖关系...
正在查找软件包冲突...
 
软件包 (1) curl-7.70.0-1
 
全部安装大小：  0.85 MiB
净更新大小：  0.00 MiB
 
:: 进行安装吗？ [Y/n]
```
##### 云端
pacman仓库地址：https://repo.msys2.org/msys/x86_64/  

镜像地址：https://mirror.jmu.edu/pub/msys2/msys/x86_64/  
镜像地址2：https://ftp.osuosl.org/pub/msys2/msys/x86_64/  
镜像地址3：https://download.nus.edu.sg/mirror/msys2/msys/x86_64/  

安装步骤跟上面一样，只不过路径换成云端的URL
