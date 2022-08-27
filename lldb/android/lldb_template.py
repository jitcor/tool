import os
import re
import sys
import lldb


def enter_console(command_interpreter: lldb.SBCommandInterpreter, ):
    while True:
        command = input("(lldb) ")
        if command == "q":
            return
        print(exec_lldb(command_interpreter, command))


def hexdump(command_interpreter: lldb.SBCommandInterpreter, pointer: int, size: int) -> str:
    return exec_lldb(command_interpreter, "memory read %s %s" % (pointer, pointer + size))


def get_so_base(command_interpreter: lldb.SBCommandInterpreter, so_name: str) -> int:
    result = exec_lldb(command_interpreter, "image list")
    print(result)
    return int(re.split(r" +", re.findall(r"\[.*?\\%s" % so_name, result)[0])[-2], 16)


def get_pointer_value(command_interpreter: lldb.SBCommandInterpreter, pointer: int) -> int:
    result = exec_lldb(command_interpreter, "memory read -fx -c1 %s" % pointer)
    print(result)
    return int(result.split(' ')[1], 16)


def exec_lldb(command_interpreter: lldb.SBCommandInterpreter, command: str) -> str:
    ci_result = lldb.SBCommandReturnObject()
    command_interpreter.HandleCommand(command, ci_result)
    if not ci_result.Succeeded():
        print(ci_result)
        return ""
    return ci_result.GetOutput()


def exec_android_shell(platform: lldb.SBPlatform, command: str) -> str:
    command: lldb.SBPlatformShellCommand = lldb.SBPlatformShellCommand(command)  # (shell) android shell env
    error = platform.Run(command)
    if not error.Success():
        print(error)
        return ""
    return command.GetOutput()


def do_task(debugger: lldb.SBDebugger):
    debugger.SetAsync(False)#关闭异步模式，否则控制台不会阻塞
    ci = debugger.GetCommandInterpreter()
    plat=debugger.GetSelectedPlatform()

    result = exec_android_shell(plat, "system/bin/ps -A | grep {包名} | grep -v {进一步过滤}")
    print(result)
    pid = re.split(' +', result)[1]
    print(exec_lldb(ci, "attach " + pid))

    base = get_so_base(ci, "lib{XXXXX}.so")
    print("base:", hex(base))

    XXX_ptr = get_pointer_value(ci, base + 0xbe530)
    print("interface:", hex(XXX_ptr))

    enter_console(ci)
    
    exec_lldb(ci, "detach")


if __name__ == '__main__':
    os.system(r"D:\tool\AdbTool1.0.1\adb forward tcp:8129 tcp:8129")
    os.popen(
        r"D:\tool\AdbTool1.0.1\adb shell su -c './data/local/tmp/lldb-server platform --listen \"*:8129\" --server'")

    platform: lldb.SBPlatform = lldb.SBPlatform("remote-android")
    error = platform.ConnectRemote(lldb.SBPlatformConnectOptions("connect://:8129"))
    print(error)

    debugger: lldb.SBDebugger = lldb.SBDebugger.Create()
    debugger.SetSelectedPlatform(platform)

    do_task(debugger)
    
    platform.DisconnectRemote()
    platform.Clear()
    debugger.Clear()
    lldb.SBDebugger.Destroy(debugger)
