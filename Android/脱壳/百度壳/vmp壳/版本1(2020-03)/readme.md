
# 原理解析
[百度加固免费版分析及VMP修复](https://bbs.pediy.com/thread-257926.htm)
# 工具封装小白化
https://bbs.binmt.cc/thread-43596-1-1.html
## 关键步骤
### 获取method_id
```
su
chmod 0777 ./baidudump && ./baidudump -i ./dump.dex
```
### 获取vmp_id
直接反编译dex找到目标方法中的vmp_id,类似下面这样的
```
.method xxxxx
.registers x
const vx,0x55000000
```
### 修复
```
./baidudump -d ./dump.dex 0x00000023 0x55000000
```
0x00000023是原始method_id,0x55000000 是该方法对应的vmp_id
### 注意事项
◎重新打包请自行还原原始Application名称 \
◎还原后的dex如果放进安装包闪退，可以用mt修复dex \
◎此方法仅适用于百度加固免费版(maybe 5.x)，其他壳自测 \
