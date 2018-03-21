import psutil
from subprocess import PIPE


p1= psutil.Popen('F:\software\新监测程序\监测进程.exe')
print(p1.name())

print(p1.username())

print(p1.communicate())
