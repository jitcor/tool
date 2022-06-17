# Window 还原frida-trace的c++函数名
```python
import os
import re


def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text
def fix(name):
   return execCmd('demumble.exe {}'.format(name))

if __name__ == '__main__':
    data=open("trace.log.txt",'rb').read().decode()
    for match in re.findall(r'(_Z.*?)\(\)',data):
        new=fix(match)
        data=data.replace(match,new)
        print("replace {}->{}".format(match,new))
    open("trace.log.fix.txt", 'wb').write(data)
```
