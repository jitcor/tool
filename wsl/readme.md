# 简介
wsl为window子系统工具
# 安装WSL[<sup>2<sup/>](#ref2)
- `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`(PowerShell)
- 等待重启系统即可
# 安装WSL2
 - 执行命令开启系统虚拟化：`dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`(PowerShell)
 - 等待重启系统
 - `wsl --set-default-version 2`设置wsl默认版本，也就是新子系统安装时使用的wsl版本
 - `wsl -l -v`查看所有已安装子系统及其wsl版本
 - `wsl --set-version UbuntuXX 2`设置某个已安装子系统的wsl版本
# 使用ubuntu子系统
- 下载安装文件[<sup>4<sup/>](#ref4)
- `Add-AppxPackage .\app_name.appx`使用PowerShell安装该文件[<sup>q1<sup/>](#q1)
- or 直接鼠标点击打开[<sup>q1<sup/>](#q1)
- 等待系统初始化完成
- 设置用户名和密码
- `sudo su`切换到root用户(可选)
- `sudo apt-get update`(apt更新)
# wsl常用命令[<sup>1<sup/>](#ref1)
- `wsl --list`列出所有已安装系统
- `wsl --unregsiter {system name}`卸载指定系统（system name即是上面命令返回的列表字符串)
 
# remoteWSL工具(vscode插件)
- vscode搜索即可下载，安装完后点击左下角的图标(类似这样“><“的图标)
- 在子系统里进入到项目目录
- `code .`[<sup>q2<sup/>](#q2)
- 等待自动打开vscode
- 编写代码
# linux访问window目录
 - `cd /mnt/`
 - 即可看到挂载的目录
 # 开启子系统全局代理
 ## wsl1
 - `export ALL_PROXY="http://127.0.0.1:10809"`
 # WSL修改子系统目录
 ```
 wsl -l -v
 wsl --export Ubuntu-20.04 d:\ubuntu20.04.tar
 wsl --unregister Ubuntu-20.04
 wsl --import Ubuntu-20.04 d:\ubuntu d:\ubuntu20.04.tar --version 2
 del d:\ubuntu20.04.tar
 ```
 # 切换账户
 - 切换到root账户`sudo su`
 - root账户切换到普通账户`su - username`
 # WSL2设置全局代理
 ```sh
 #!/bin/bash
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")
export ALL_PROXY="http://$host_ip:10809"
echo "proxy ip:$ALL_PROXY"
 ```
 > 执行时需用source执行，否则无法生效
 # 使目录大小写敏感
 - 管理员方式执行`fsutil.exe file setCaseSensitiveInfo <path> enable`
 - 禁用则执行`fsutil.exe file setCaseSensitiveInfo <path> disable`
 - 查询则执行`fsutil.exe file queryCaseSensitiveInfo <path>`
# 问题
## q1.`The system can not find the file specified.`<a id="q1"/> 
 If you have downloaded the Appx file then extract it with any unzipping tool (for example 7zip) in a folder and run the ubuntu.exe in it.
## q2.linux系统默认没有导入window path问题，导致一些window下的命令在子系统里找不到<a id="q2"/> 
 在/etc/wsl.conf文件（没有则touch一个）里加入如下代码:
 ```ini
[interop]
enabled = true
appendWindowPath = true
 ```
## q3.vscode 的remoteWSL 不能编辑root权限的文件[<sup>3<sup/>](#ref3) 
 `ubuntu.exe config --default-user root`
 ## q4.参考的对象类型不支持尝试的操作(WSL2)
 - 下载NoLsp.exe
 - 管理员CMD/PowerShell执行`NoLsp.exe C:\windows\system32\wsl.exe`
## q4. `error: chmod on /aosp/.repo/repo/.git/config.lock failed: Operation not permitted`
 参考https://github.com/docker/for-win/issues/6284 \
 参考https://devblogs.microsoft.com/commandline/chmod-chown-wsl-improvements/
 - 第一个方案就是把文件放在WSL自己的文件系统里
 - 第二个就是采用官方的Chmod支持插件
 # 参考
 - 1.[WSL 命令和启动配置](https://docs.microsoft.com/zh-cn/windows/wsl/wsl-config#set-wsl-launch-settings)<a id="ref1"/>
 - 2.[适用于 Linux 的 Windows 子系统安装指南 (Windows 10)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)<a id="ref2"/>
 - 3.[WSL中的VSCode：如何对根文件进行sudo，以便我可以对其进行编辑](https://stackoverflow.com/questions/58980356/vscode-in-wsl-how-to-sudo-a-root-file-so-i-can-edit-it)<a id="ref3"/>
 - 4.[手动下载适用于 Linux 的 Windows 子系统发行版包](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual)<a id="ref4"/>
