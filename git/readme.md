# 查看git代理状态
```
git config --global --get http.proxy
```
# 设置Http代理
```
git config --global http.proxy http://127.0.0.1:10809
git config --global https.proxy https://127.0.0.1:10809
```
# 设置socks代理
```
git config --global http.proxy 'socks5://127.0.0.1:10808'
git config --global https.proxy 'socks5://127.0.0.1:10808'
```

# 解除代理
```
git config --global --unset http.proxy
git config --global --unset https.proxy
```
# 删除commit-1
```
git log # 查看commit 历史
git reset --hard HEAD^ # 回滚到上次提交
git reset --hard xxxxx  # 回滚到xxxxx提交
git push origin master -f # 提交删除操作
```
# 删除commit-2
```
git log # 查看commit 历史
git rebase -i xxxxxx # xxxxx为目标commit的前一个commit
然后drop掉目标commit
git push origin master -f # 提交删除操作
```
# 删除初次提交
```
修改文件
git add .   # 添加修改
git commit --amend -m 'initial commit'  # 提交修改（但其实是修改的上一次提交）
git push origin main -f  # 上传修改
```
> 在第一次提交之前没有任何东西，因为每次提交都引用一个父提交。这使得第一次提交是特殊的(孤立提交)，所以没有办法引用以前的“状态”。
因此，如果您想修复提交，您可以简单地git commit --amend：这将修改提交，而不创建另一个提交。
如果只是想重新开始，可以删除.git存储库，然后使用git init创建另一个存储库  
refs:https://cloud.tencent.com/developer/ask/sof/77445   
