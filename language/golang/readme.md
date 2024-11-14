# 多版本golang共存
```cmd
# 还能 get 其他版本的golang
$ go get golang.org/dl/go1.15.2
# 新版方式
$ go install golang.org/dl/go1.20.9@latest
# 版本列表：https://go.dev/dl/

# 下载这一步不能少
$ go1.15.2 download

# 检查下吧
$ go1.15.2 version
go version go1.15.2 windows/amd64

# 默认的 golang 版本
$ go version
go version go1.13.14 windows/amd64
```
参考https://golang.org/doc/manage-install#installing-multiple
