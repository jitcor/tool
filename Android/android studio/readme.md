# AS 使用的adb与系统的adb不是同版本时解决方案，并且两个adb文件在不同的磁盘分区
- 执行如下命令，对应目录和文件需要自行替换下
```cmd
mklink /J "E:\tool\sdk\platform-tools" "D:\tool\sdk-mirror\platform-tools" # 将AS使用的adb所在目录移动到与系统adb同磁盘分区下，然后执行该条命令进行目录链接，让AS还能在原始目录下找到adb文件，若是两个adb文件在同一个磁盘分区，可以不用执行该条命令
mklink /H "D:\tool\sdk-mirror\platform-tools\adb.exe" "D:\tool\AdbTool1.0.1\adb.exe" # 将移动后的adb文件删除或备份下，然后执行该条命令，将系统adb链接到AS的adb，然后AS再执行adb命令就是执行的系统adb了
```
> 注：若是移动文件(夹)时，提示占用，可以采用[windows查看文件被哪个进程占用](https://blog.csdn.net/u010999809/article/details/98308622?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522161240659916780271535382%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fall.%252522%25257D&request_id=161240659916780271535382&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_v2~rank_v29-1-98308622.pc_search_result_no_baidu_js&utm_term=window+%25E6%259F%25A5%25E6%2589%25BE%25E6%2596%2587%25E4%25BB%25B6%25E5%258D%25A0%25E7%2594%25A8%25E8%25BF%259B%25E7%25A8%258B)查找占用的进程
# 参考
- [windows系统下的文件夹链接功能mklink/linkd](https://www.cnblogs.com/plusium/archive/2010/03/17/1688511.html)
