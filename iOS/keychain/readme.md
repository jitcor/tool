## Keychain_Dumper
### FAQ
- Q:
```
dyld: Symbol not found: _objc_release_x19
  Referenced from: /private/var/tmp/./keychain_dumper (which was built for iOS 16.4)
  Expected in: /usr/lib/libobjc.A.dylib

Abort trap: 6
```
- A:
```
重新编译keychain_dumper，更改makefile里SDK变量为当前iOS设备对应版本的TheOS SDK：https://github.com/theos/sdks，参考：https://github.com/ptoomey3/Keychain-Dumper/issues/71
```
- Q:
```
[INFO] No Generic Password Keychain items found.
[HINT] You should unlock your device!
[INFO] No Internet Password Keychain items found.
[HINT] You should unlock your device!
```
- A:
```
修改权利文件：entitlements.xml里的keychain-access-groups里的'*'号为指定的要获取的钥匙串访问组，比如Zoom的BJ4HAAB9B3.us.zoom.meetings.keychain.share，然后重新编译签名即可
```
