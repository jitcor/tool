# 解BL锁
- 开启oem
- fastboot oem unlock
> 注：解BL锁后，Wlan无法正常使用了，即使完全还原也不行，可能需要升级到最新版固件包才能解决(更新:据酷安网友说需要刷persist分区才行，具体待测试)
# Magisk
- 下载固件包[https://www.h2os.com/download.](https://www.h2os.com/download.)
- 解包提取boot.img
- Magisk 对boot.img打补丁
- fastboot boot magisk_patch.img
- 后面按提示操作即可
# 解包提取boot.img
- 下载解包工具https://gist.github.com/ius/42bd02a5df2226633a342ab7a9c60f15
- 包含两个py文件payload_dumper.py，update_metadata_pb2.py
- 或者直接当前目录下载即可
- pip3 install protobuf
- python payload_dumper.py payload.bin (payload.bin从固件包里提取即可)
