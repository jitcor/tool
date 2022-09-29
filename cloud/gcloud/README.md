# 下载
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe?hl=zh-cn
# 安装
一路Next即可
# 初始化
```
gcloud init
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

# ping 测试
https://www.boce.com/ping/xxx.xx.xxx

# 参考
- [cloud run](https://cloud.google.com/run?hl=zh-cn)
- [install](https://cloud.google.com/sdk/docs/install?hl=zh-cn)
- [initializing](https://cloud.google.com/sdk/docs/initializing?hl=zh-cn)
- [install-sdk](https://cloud.google.com/sdk/docs/install-sdk?hl=zh-cn)
- [deploy-go-service](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-go-service?hl=zh-cn)
