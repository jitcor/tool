 # 安装
 ```
 pip3 install objection -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
 ```
# 注入
## iOS
```
objection -d --gadget "微信" explore
```
#### keychain 
- 简略打印版
```
(objection): ios keychain dump_raw
```
- 完整文件版(v_data是完整数据，键值对的名字是完整名字)
```
(objection): ios keychain dump --json keychain_dump.json
```
> 保存目录：当前MacOS电脑运行命令路径
## Android
#### ImportError: cannot import name 'escape' from 'jinja2' 错误
- 将jinja2降低到3.0.3版本即可
```
pip3 install jinja2==3.0.3 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
# 参考
- [iOS Hooking With Objection](https://book.hacktricks.xyz/mobile-apps-pentesting/ios-pentesting/ios-hooking-with-objection)
- [ImportError: cannot import name 'escape' from 'jinja2'](https://stackoverflow.com/questions/71718167/importerror-cannot-import-name-escape-from-jinja2)
