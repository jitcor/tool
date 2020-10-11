# 设置代理
- 解决ppa.launchpad.net下载慢问题
- 在/etc/apt/apt.conf文件下加入如下内容，并修改成自己的代理
```
Acquire::http::proxy "http://127.0.0.1:10809/";
Acquire::https::proxy "https://127.0.0.1:10809/";
```
- apt-get update
- apt-get install xxxx
