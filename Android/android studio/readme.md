# AS 使用的adb与系统的adb不是同版本时解决方案，并且两个adb文件在不同的磁盘分区
- 执行如下命令，对应目录和文件需要自行替换下
```cmd
mklink /J "E:\tool\sdk\platform-tools" "D:\tool\sdk-mirror\platform-tools" # 将AS使用的adb所在目录移动到与系统adb同磁盘分区下，然后执行该条命令进行目录链接，让AS还能在原始目录下找到adb文件，若是两个adb文件在同一个磁盘分区，可以不用执行该条命令
mklink /H "D:\tool\sdk-mirror\platform-tools\adb.exe" "D:\tool\AdbTool1.0.1\adb.exe" # 将移动后的adb文件删除或备份下，然后执行该条命令，将系统adb链接到AS的adb，然后AS再执行adb命令就是执行的系统adb了
```
# 参考
- [windows系统下的文件夹链接功能mklink/linkd](https://www.cnblogs.com/plusium/archive/2010/03/17/1688511.html)
