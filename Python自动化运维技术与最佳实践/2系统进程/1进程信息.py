import psutil
print(psutil.pids())
a= psutil.Process(1072)
print(a.name())
#1072就是SVN客户端
print(a.exe())
#进程bin路径
print(a.cwd())
#进程工作目录的路径

print(a.status())

#print(a.uids())
#print(a.gids())
print(a.memory_percent())
