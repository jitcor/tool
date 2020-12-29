# 编译环境配置 ([官方配置要求](https://source.android.com/source/requirements?hl=zh-cn))
# JDK配置([JDK要求](https://source.android.com/source/requirements?hl=zh-cn#jdk))
```
Android 7.0 (Nougat) - Android 8.0 (O)：Ubuntu - OpenJDK 8；Mac OS - jdk 8u45 或更高版本
Android 5.x (Lollipop) - Android 6.0 (Marshmallow)：Ubuntu - OpenJDK 7；Mac OS - jdk-7u71-macosx-x64.dmg
Android 2.3.x (Gingerbread) - Android 4.4.x (KitKat)：Ubuntu - Java JDK 6；Mac OS - Java JDK 6
Android 1.5 (Cupcake) - Android 2.2.x (Froyo)：Ubuntu - Java JDK 5
```
# Make 配置
```
Android 4.0.x (Ice Cream Sandwich) 及更低版本需要将 make 3.82 还原到较低版本，以避免出现编译错误
```
# python3.6+配置

# 详细步骤
```
mkdir ~/bin
PATH=~/bin:$PATH
curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
chmod a+x ~/bin/repo
mkdir source
cd source
repo init -u https://android.googlesource.com/platform/manifest -b android-4.4.4_r1
repo sync
```
- 配置代理参见[tool/proxy](https://github.com/ihbing/tool/tree/master/proxy)
- 提示配置用户和邮箱时随便配置即可
- sync过程中有报以下错误
```
error: RPC failed; curl 56 GnuTLS recv error (-9): A TLS packet with unexpected length was received.
fatal: The remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
platform/bootable/recovery:
remote: Counting objects: 28282, done.
remote: Compressing objects: 100% (1106/1106), done.
error: RPC failed; curl 56 GnuTLS recv error (-9): A TLS packet with unexpected length was received.
fatal: The remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
```
# 参考
-1.[AOSP 编译和烧写](http://blog.hanschen.site/2019/09/12/aosp_compile_and_flash/)
