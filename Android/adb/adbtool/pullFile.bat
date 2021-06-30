set /p remotePath=please input remote path:
call adb pull %remotePath% %1