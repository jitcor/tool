# 下载
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe?hl=zh-cn
# 安装
一路Next即可
# 初始化
```
gcloud init
```
# 配置代理
```
gcloud config set proxy/type http

gcloud config set proxy/address 127.0.0.1

gcloud config set proxy/port 7890
```

# go代码配置http服务器HelloWorld
### 列出已有项目ID
```
gcloud projects list --format="value(projectId)"
```
> 这个项目ID就是云端控制台已有项目的ID
### 设置项目ID
```
 gcloud config set project {PROJECT_ID}
```
> 部署在哪个项目下
### 部署项目到云端
```
gcloud run deploy
```
> 按提示操作即可
# 常用命令
### 查看所有项目
```
gcloud projects list --format="value(projectId)"
```
### 登录账号
```
gcloud auth login
```
### 列出账号
```
gcloud auth list
```
# 注意事项
### gcloud 网域映射限制
https://cloud.google.com/run/docs/mapping-custom-domains?_ga=2.79877783.-1055374585.1664688564#limitations
### 免费试用升级账号导致扣费问题
ref:[免费试用结束](https://cloud.google.com/free/docs/free-cloud-features?hl=zh-CN#end)  
解决方案参考：https://lebang2020.cn/details/201204scdock02.html  
右上角问号->GCP结算支持->根据提示进行操作即可->最后联系到人工客户，说明自己情况->等待处理结果  

# ping 测试
https://www.boce.com/ping/xxx.xx.xxx
# google 域名注册
https://domains.google.com/
# 参考
- [cloud run](https://cloud.google.com/run?hl=zh-cn)
- [install](https://cloud.google.com/sdk/docs/install?hl=zh-cn)
- [initializing](https://cloud.google.com/sdk/docs/initializing?hl=zh-cn)
- [install-sdk](https://cloud.google.com/sdk/docs/install-sdk?hl=zh-cn)
- [deploy-go-service](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-go-service?hl=zh-cn)
