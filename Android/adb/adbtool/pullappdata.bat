set /p package=please input package:
call adb shell "su -c 'setenforce 0'"
call adb shell "su -c 'rm -rf /sdcard/adbtool/%package%/'"
call adb shell "su -c 'mkdir -p /sdcard/adbtool/%package%/'"
call adb shell "su -c 'cp -r /data/data/%package%/ /sdcard/adbtool/'"
call adb pull /sdcard/adbtool/%package%/ %1
# call adb shell "su -c 'rm -rf /sdcard/adbtool/%package%/'"