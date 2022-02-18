# 官方
https://github.com/avast/retdec/
# 安装
## Window
> 前提条件：1.安装 [Microsoft Visual C++ Redistributable for Visual Studio 2017](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads).\
> 前提条件：2.[Python](https://www.python.org/) (version >= 3.4)

- 下载https://github.com/Humenger/tool/releases/tag/retdec
- 解压
# 使用
## Window
- 反编译armeabi-v7a的so
```
python ../retdec-v4.0-windows-32b\retdec\bin\retdec-decompiler.py libwb_security.so
```
- 输出结果\
[!image](./images/retdec_done.png)
# 参考
- https://www.bookstack.cn/read/CTF-All-In-One/doc-5.11.1_retdec.md
- 
