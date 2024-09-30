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
# 例子:facebook的homebrew-fb
git -C "$(brew --repo facebook/fb)" remote set-url origin https://gitclone.com/github.com/facebook/homebrew-fb.git
```
## 查看代理
brew 使用的是curl，所以查看curl的代理即可，如何查看呢？可以在`curl http://google.com -v`看一下输出
## 设置代理
命令行形式。形如`curl http://google.com -x http://127.0.0.1:7890`或者`curl http://google.com -x socks4://127.0.0.1:1089` \
curl的代理配置文件在`~/.curlrc`文件里，格式如下 \
http 
```
proxy = "127.0.0.1:7890"
```
或者 \
socks5 
```
socks5 = "127.0.0.1:1089"
```
但socks5未测试成功，即使以命令行-x 选项也不行，可能是代理的问题 

但是该方式测试失败，测试环境如下：
- macOS Catalina 10.15.7
- brew 3.2.9
经查是由于其在使用curl工具时有个`--disabale`选项，该选项禁止了.curlrc文件方式
- 最终成功方法是
```
export ALL_PROXY=socks5://127.0.0.1:1089
```
# 权限问题
brew在安装某些软件时会涉及到/usr/local/目录的读写权限，会出现类似如下错误 
```
Error: /usr/local/Cellar/buck/2021.01.12.01 is not a directory
```
这时执行
```
sudo chown -R $(whoami) /usr/local/Cellar/
```
即可，但又会出现另一个问题
```
Error: Failure while executing; `cp -pR /private/tmp/d20210826-15074-zh9zmn/buck/. /usr/local/Cellar/buck` exited with 1. Here's the output:
cp: /usr/local/Cellar/buck/./2021.01.12.01_1/bin/buck: Permission denied
```

# 常用工具
## libusb
```
brew install libusb
# 查看安装路径
brew info libusb
# 将路径添加到系统查找目录
export DYLD_LIBRARY_PATH="/usr/local/Cellar/libusb/1.0.27/lib:$DYLD_LIBRARY_PATH"
```
