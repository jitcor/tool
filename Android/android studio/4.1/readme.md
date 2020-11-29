# 开启v2rayN代理
开启Http代理并自动配置系统代理
# 配置gradle代理
- 路径C:\Users\user\.gradle\gradle.properties
```
systemProp.http.proxyHost=127.0.0.1
systemProp.http.proxyPort=10809
systemProp.https.proxyHost=127.0.0.1
systemProp.https.proxyPort=10809
```
# 打不开问题
- 1.提示如下
```
Missing essential plugin:

  org.jetbrains.android

Please reinstall Android Studio from scratch.
```
- 删除文件C:\Users\YourUserName\AppData\Roaming\Google\AndroidStudioPreview4.1\disabled_plugins.txt
