## 更新PowerShell
- 安装新版本：`iex "& { $(irm https://aka.ms/install-powershell.ps1 -UseBasicParsing) }"`
- 设为默认版本
  - 点击设置
  ![img](res/powershell_settings.png)
  - 点击`添加新配置文件`
  - 将新版本的powershell路径添加进去
  - 然后在启动选项里将该新配置设置默认配置文件
## 添加命令别名
> 注意不是PowerShell里的Alias别名
- 执行echo $PROFILE命令，确定新建文件的名称和位置
- touch $PROFILE 创建该文件(若没有的话)
- 按如下格式添加命令
```
function 别名 { 需要替代的命令 }
```
eg.
```
function history { cat C:\Users\xxx\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt }
```
- 然后执行`Set-ExecutionPolicy RemoteSigned` 生效更改
- 重启PowerShell即可
