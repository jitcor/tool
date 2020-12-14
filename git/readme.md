# 查看git代理状态
```
git config --global --get http.proxy
```
# 设置Http代理
```
git config --global https.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080
```
# 设置socks代理
```
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'
```

# 解除代理
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
