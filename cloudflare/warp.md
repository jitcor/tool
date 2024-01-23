## 注册账户

## ubuntu
参考：https://developers.cloudflare.com/warp-client/get-started/linux/  
- 安装
```
# Add cloudflare gpg key
curl -fsSL https://pkg.cloudflareclient.com/pubkey.gpg | sudo gpg --yes --dearmor --output /usr/share/keyrings/cloudflare-warp-archive-keyring.gpg


# Add this repo to your apt repositories
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/cloudflare-warp-archive-keyring.gpg] https://pkg.cloudflareclient.com/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/cloudflare-client.list


# Install
sudo apt-get update && sudo apt-get install cloudflare-warp
```
- 使用
```
# 直接上plus，现在直接注册的共享账户已经不能用了，<Name> 替换成你在官网(1.1.1.1)申请的团队名字，
warp-cli teams-enroll <Name>
然后会返回一个链接：
https://<Name>.com.cloudflareaccess.com/warp
在浏览器打开，输入个邮箱验证，该邮箱domain需要符合你的团队domain要求，验证完后，就注册设备成功了

然后出现一个成功的页面，在该页面检查源代码(ref:[参考文档](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/manual-deployment/))

找到如下代码，url后面的内容就是token
<meta http-equiv="refresh" content"=0;url=com.cloudflare.warp://acmecorp.cloudflareaccess.com/auth?token=yeooilknmasdlfnlnsadfojDSFJndf_kjnasdf..." />

然后执行下面这条命令
warp-cli teams-enroll-token com.cloudflare.warp://<your-team-name>.cloudflareaccess.com/auth?token=<your-token>
等待返回success

再执行
warp-cli connect 
等待连接成功

再执行
warp-cli status
查看状态
显示
connected
表示连接成功

再执行
curl https://www.cloudflare.com/cdn-cgi/trace/
查看是否有
warp=plus
则表示切换到了plus版
```

![image-20240124033941291](./warp/image-20240124033941291.png)

![image-20240124034400230](./warp/image-20240124034400230.png)

