# 隐藏窗口启动
```vbs
 Set ws = CreateObject("Wscript.Shell") 
   ws.run "cmd /k E:\tool\frp\frp_0.33.0_windows_amd64\frpc.exe -c E:\tool\frp\frp_0.33.0_windows_amd64\frpc.ini",vbhide
   
```
