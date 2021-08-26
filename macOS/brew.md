# 墙问题

## 查看源
```
# 查看 brew.git 当前源
$ cd "$(brew --repo)" && git remote -v
origin    https://github.com/Homebrew/brew.git (fetch)
origin    https://github.com/Homebrew/brew.git (push)

# 查看 homebrew-core.git 当前源
$ cd "$(brew --repo homebrew/core)" && git remote -v
origin    https://github.com/Homebrew/homebrew-core.git (fetch)
origin    https://github.com/Homebrew/homebrew-core.git (push)

# 查看XXXX的源
$ cd "$(brew --repo xxxxx)" && git remote -v
```
## 替换源
```
# 修改 brew.git 为阿里源
$ git -C "$(brew --repo)" remote set-url origin https://mirrors.aliyun.com/homebrew/brew.git

# 修改 homebrew-core.git 为阿里源
$ git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.aliyun.com/homebrew/homebrew-core.git

# 修改 xxxx的源，后面的xxxxxxxxxxxxxxxxx参考上面设置，也就是其仓库地址，这里可以使用https://codechina.csdn.net/mirrors克隆github仓库，然后替换地址
$ git -C "$(brew --repo xxxxx)" remote set-url origin xxxxxxxxxxxxxxxxxxxxxx

```
## 查看代理
brew 使用的是curl，所以查看curl的代理即可，如何查看呢？可以在`curl http://google.com -v`看一下输出
## 设置代理
命令行形式。形如`curl http://google.com -x http://127.0.0.1:7890`或者`curl http://google.com -x socks4://127.0.0.1:1089` \
curl的代理配置文件在`~/.curlrc`文件里，格式如下
http \
```
proxy = "127.0.0.1:7890"
```
或者
socks5 \
```
socks5 = "127.0.0.1:1089"
```
但socks5未测试成功，即使以命令行-x 选项也不行，可能是代理的问题 \







