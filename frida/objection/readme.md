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
```
(objection): ios keychain dump_raw
```
## Android
#### ImportError: cannot import name 'escape' from 'jinja2' 错误
- 将jinja2降低到3.0.3版本即可
```
pip3 install jinja2==3.0.3 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```
# 参考
- [iOS Hooking With Objection](https://book.hacktricks.xyz/mobile-apps-pentesting/ios-pentesting/ios-hooking-with-objection)
- [ImportError: cannot import name 'escape' from 'jinja2'](https://stackoverflow.com/questions/71718167/importerror-cannot-import-name-escape-from-jinja2)
