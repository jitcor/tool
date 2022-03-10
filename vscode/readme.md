# 问题
- 1.ctrl+c，光标变粗问题
> 卸载或禁用vim插件
# remote-ssh问题
## openssh-server
```
dpkg -l | grep ssh //check ssh-server
sudo apt-get install openssh-server
```
关于报错
```
下列软件包有未满足的依赖关系：
 openssh-server : 依赖: openssh-client (= 1:6.6p1-2ubuntu1)
E: 无法修正错误，因为您要求某些软件包保持现状，就是它们破坏了软件包间的依赖关系。
```
直接`sudo apt-get install openssh-client=1:6.6p1-2ubuntu1`
## ssh config
```
Host 47.xx.xx.11
  HostName 47.xx.xx.11
  User root
  Port 22
  IdentityFile C:\Users\Administrator\.ssh\id_rsa.pub

```
> cat id_rsa.pub >> ~/.ssh/authorized_keys # id_rsa.pub由本地上传到服务端，然后在服务端执行该命令，之后就可以正常连接了
## 无法连接问题
![image](https://user-images.githubusercontent.com/27600008/128586497-ef6d7c3b-0fb5-4730-85ae-81df3c66d5bb.png)
- id_rsa.pub文件的权限太开放，改成如下仅有一个用户，并且权限改成只读
![image](https://user-images.githubusercontent.com/27600008/128586535-acccd6db-6aa0-4a17-aab5-c8bbea401036.png)

