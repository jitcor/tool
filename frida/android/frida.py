import os
import frida
import sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message['description'])


def injectProcess(packageName, jsPath, isReboot=False, ip=None, port=None):
    # 获取设备
    device = frida.get_remote_device() if ip is None and port is None else frida.get_device_manager().add_remote_device(
        '{host}:{port}'.format(
            host=ip, port=port))
    # 注入进程
    if isReboot:
        pid = device.spawn(packageName)
        process = device.attach(pid)
    else:
        process = device.attach(packageName)
    # 创建脚本
    js = open(jsPath, 'r', encoding='UTF-8').read()
    script = process.create_script(js)
    # 绑定函数
    script.on('message', on_message)
    # 加载脚本
    script.load()
    if isReboot:
        device.resume(pid)
    print("common_enabled_debug running....")
    # 执行脚本
    sys.stdin.read()
