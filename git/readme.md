## 查看git代理状态
```
git config --global --get http.proxy
```
## 设置Http代理
```
git config --global http.proxy http://127.0.0.1:7890
git config --global https.proxy https://127.0.0.1:7890
```
## 设置socks代理
```
git config --global http.proxy 'socks5://127.0.0.1:7890'
git config --global https.proxy 'socks5://127.0.0.1:7890'
```

## 解除代理
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
## 完全撤回commit（直接在git log里看不到这条commit记录）
> 注：带--hard的会删除本地更改的代码
### 方案1
```
git checkout <branch>  # 先切换到目标分支
git log # 查看commit 历史
git reset --hard HEAD^ # 回滚到上次提交
git reset --hard xxxxx  # 回滚到xxxxx提交
git push origin <branch> -f # 提交删除操作
```
### 方案2
```
git checkout <branch>  # 先切换到目标分支
git log # 查看commit 历史
git rebase -i xxxxxx # xxxxx为目标commit的前一个commit
然后drop掉目标commit
git push origin <branch> -f # 提交删除操作
```
### 初次提交
```
修改文件
git checkout <branch>  # 先切换到目标分支
git add .   # 添加修改
git commit --amend -m 'initial commit'  # 提交修改（但其实是修改的上一次提交）
git push origin <branch> -f  # 上传修改
```
> 在第一次提交之前没有任何东西，因为每次提交都引用一个父提交。这使得第一次提交是特殊的(孤立提交)，所以没有办法引用以前的“状态”。
因此，如果您想修复提交，您可以简单地git commit --amend：这将修改提交，而不创建另一个提交。
如果只是想重新开始，可以删除.git存储库，然后使用git init创建另一个存储库  
refs:https://cloud.tencent.com/developer/ask/sof/77445   
refs:https://blog.csdn.net/CHAOS_ORDER/article/details/122655480
## 修改commit
> 这部分仅适合没有git push 提交的，若是已经提交的，则仅能使用上面的命令才行
### 修改最新commit
```
git reset HEAD~1 # 相当于git reset --mixed HEAD~1 会撤销add和commit
# 正常修改代码
# 再次add和commit即可
```
### 修改上一次commit
```
git reset HEAD~2
# 正常修改代码
# 再次add和commit即可
```
## git选项
### git reset
```
git reset --soft 	完全保留工作区和暂存区，会撤销git commit提交，保留git add操作的内容（所有reset都会执行这个操作）
					
git reset --mixed  	完全保留工作区，会撤销commit提交和git add操作 （默认选项）

git reset --hard  	彻底清除工作区和暂存区，***慎用***

git reset --keep 	保留工作区和HEAD之间的差异

```
### HEAD~N or HEAD^N
替代commit id，表示距离HEAD之前的第N次commit id  
另附：很好的一张解释图  
```
G   H   I   J
 \ /     \ /
  D   E   F
   \  |  / \
    \ | /   |
     \|/    |
      B     C
       \   /
        \ /
         A

A =      = A^0
B = A^   = A^1     = A~1
C = A^2
D = A^^  = A^1^1   = A~2
E = B^2  = A^^2
F = B^3  = A^^3
G = A^^^ = A^1^1^1 = A~3
H = D^2  = B^^2    = A^^^2  = A~2^2
I = F^   = B^3^    = A^^3^
J = F^2  = B^3^2   = A^^3^2
```
> ref:https://stackoverflow.com/questions/2221658/whats-the-difference-between-head-and-head-in-git

