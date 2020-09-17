# 简介
wsl为window子系统工具
# 安装WSL[<sup>2<sup/>](#ref2)
- `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`(PowerShell)
- 等待重启系统即可
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
# 问题
- q1.`The system can not find the file specified.`<a id="q1"/> \
 If you have downloaded the Appx file then extract it with any unzipping tool (for example 7zip) in a folder and run the ubuntu.exe in it.
 - q2.linux系统默认没有导入window path问题，导致一些window下的命令在子系统里找不到<a id="q2"/> \
 在/etc/wsl.conf文件（没有则touch一个）里加入如下代码:
 ```ini
[interop]
enabled = true
appendWindowPath = true
 ```
 - q3.vscode 的remoteWSL 不能编辑root权限的文件[<sup>3<sup/>](#ref3) \
 `ubuntu.exe config --default-user root`
 # 参考
 - 1.[WSL 命令和启动配置](https://docs.microsoft.com/zh-cn/windows/wsl/wsl-config#set-wsl-launch-settings)<a id="ref1"/>
 - 2.[适用于 Linux 的 Windows 子系统安装指南 (Windows 10)](https://docs.microsoft.com/zh-cn/windows/wsl/install-win10)<a id="ref2"/>
 - 3.[WSL中的VSCode：如何对根文件进行sudo，以便我可以对其进行编辑](https://stackoverflow.com/questions/58980356/vscode-in-wsl-how-to-sudo-a-root-file-so-i-can-edit-it)<a id="ref3"/>
 - 4.[手动下载适用于 Linux 的 Windows 子系统发行版包](https://docs.microsoft.com/zh-cn/windows/wsl/install-manual)<a id="ref4"/>
