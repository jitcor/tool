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
# 直接上plus，现在直接注册的共享账户已经不能用了，<Name> 替换成你在官网申请的团队名字，
warp-cli teams-enroll <Name>

```

