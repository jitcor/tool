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





