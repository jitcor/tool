# 概念解释
simg: sparse ext4 image  
# 工具
- simg2img (将sparse格式镜像转为raw镜像)
- img2simg (上面的逆向)
- dumpe2fs （dump ext2文件系统信息）
- file （查看各种文件格式信息）
- mount （挂载文件系统）
- umount （解除挂载文件系统）
# 解包
```
$> PATH=$PATH:/data/tool/android/android-10.0.0_r2/out/host/linux-x86/bin/
$> simg2img system.img system.img.raw
$> mkdir /mnt/system -p
$> sudo mount system.img.raw /mnt/system -o ro
$> sudo mount -o remount,rw /mnt/system/
$> cd /mnt/system/
```
## 错误处理
- `mount: /mnt/system: wrong fs type, bad option, bad superblock on /dev/loop7, missing codepage or helper program, or other error.`
> mount 里添加-o ro 选项，也就是以只读方式挂载，然后重新挂载读写就会出现下面的问题
- `mount: /mnt/system: cannot remount /dev/loop7 read-write, is write-protected`
> 被写保护了
# 参考
- [Android 10 根文件系统和编译系统(二)：Android ROM镜像介绍](https://blog.csdn.net/ldswfun/article/details/119786846)
