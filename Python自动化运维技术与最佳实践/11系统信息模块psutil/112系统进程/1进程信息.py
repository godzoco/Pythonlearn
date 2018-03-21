import psutil
print(psutil.pids())
a = psutil.Process(3444)
print(a.name())

#这个程序流程，可能在window上有权限不足的问题
#这个3444是PDF的阅读工具就可以，某些PID有权限不足不能运行
print(a.exe())
print(a.cwd())
print(a.status())

print(a.memory_percent())
