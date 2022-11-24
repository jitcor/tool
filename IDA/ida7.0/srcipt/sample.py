import sys
# 引入ida提供给我们的api
import idaapi
# 引入pyqt，编写交互界面
from PyQt5 import QtWidgets
 
# 这里一定要继承ida提供的插件的base类
class RoyHook(idaapi.plugin_t):
    flags = idaapi.PLUGIN_KEEP
    comment = "royhook a ida pro plugin"
    help = ""
    # ida插件的名字
    wanted_name = "royhook"
    # ida插件的快捷键
    wanted_hotkey = "Alt+F6"
    windows = None
 
    def __init__(self):
        super(RoyHook, self).__init__()
        flags = idaapi.PLUGIN_KEEP
        pass
 
    # 脚本初始化的时候调用
    def init(self):
        return idaapi.PLUGIN_OK
 
    # 初始化后开始运行的时候调用
    def run(self, arg):
        idaapi.require('view')
        idaapi.require('view.main_view')
        main_window = view.main_view.MainView()
        if self.windows is None or not self.windows.isVisible():
            self.windows = QtWidgets.QMainWindow()
            main_window.setupUi(self.windows)
            self.windows.showNormal()
        pass
    # 脚本结束的时候调用
    def term(self):
        return idaapi.PLUGIN_OK
