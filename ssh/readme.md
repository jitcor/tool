# XShell5
https://www.banwagongzw.com/108.html
# 配置自动登录
```
echo <rsa_pub_data> > ~/.ssh/authorized_keys
# 权限配置
drwx------ 2 u0_a278 u0_a278 3452 Sep 21 15:44 .ssh
-rw------- 1 u0_a278 u0_a278    0 Sep 21 15:44 authorized_keys
# 客户端配置
# 文件：~/.ssh/config
Host 127.0.0.1
    HostName 127.0.0.1
    User u0_a278
    Port 8022
    IdentityFile C:\Users\shlu\.ssh\id_rsa
```
