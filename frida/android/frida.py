# coding=utf-8
import frida
import sys
import os
import telnetlib
import socket

default_ip = '127.0.0.1'
default_port = 27042
default_frida_server_name = 'frida_server'
# 输出frida版本
print('frida version:' + frida.__version__)


def on_message(message, data):
    type = message["type"]
    msg = message
    if type == "send":
        msg = message["payload"]
    elif type == 'error':
        msg = message['stack']
    else:
        msg = message
    print(msg)


def inject_process(package_name, js_path, is_reboot=False, ip=default_ip, port=default_port,
                   frida_server=default_frida_server_name, is_clear_data=False):
    start_server(frida_server, ip, port)
    # 清除数据
    if is_clear_data: clear_application_data(package_name)
    # 获取设备
    device = frida.get_device_manager().add_remote_device('{host}:{port}'.format(host=ip, port=port))
    # 注入进程
    if is_reboot:
        pid = device.spawn(package_name)
        process = device.attach(pid)
    else:
        process = device.attach(package_name)
    # 创建脚本
    js = open(js_path, 'r', encoding='UTF-8').read()
    script = process.create_script(js)
    # 绑定函数
    script.on('message', on_message)
    # 加载脚本
    script.load()
    if is_reboot:
        device.resume(pid)
    print("common_enabled_debug running....")
    # 执行脚本
    sys.stdin.read()


def start_server(frida_server_name, ip=default_ip, port=default_port):
    if check_frida_server(ip, port): return
    os.system('adb forward tcp:{port} tcp:{port}'.format(port=port))
    # os.system('adb forward tcp:27043 tcp:27043')
    os.system('adb shell su -c "setenforce 0"')
    os.system('adb shell su -c "chmod 777 /data/local/tmp/' + frida_server_name + '"')
    os.system('start cmd.exe /c "adb shell su -c "./data/local/tmp/' + frida_server_name + '""')
    while not check_frida_server(ip, port): pass


def check_frida_server(ip=default_ip, port=default_port):
    try:
        tcp = socket.socket()
        tcp.settimeout(2)
        tcp.connect((ip, port))
        tcp.send(b'\x00AUTH\r\n')
        res = tcp.recv(100)
        return str(res).find('REJECTED') >= 0
    except Exception as e:
        return False


def clear_application_data(package_name):
    os.system('adb shell pm clear ' + package_name)


if __name__ == '__main__':
    # start_server('fs12116')
    print("ret:", check_frida_server())
