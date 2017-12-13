#!/usr/bin/env python3

# Chapter 9 Practice Selective Copy
# Walks through a directory tree searching for files > 100MB and deletes them.

import os
os.chdir('e:\\')
def deleteUnneeded(folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(foldername + '/' + filename)
            #os.path.getsize(path)  #返回文件大小，如果文件不存在就返回错误
            print(fileSize)
            if int(fileSize) < 10000000:
                #这个10000000 是100MB  是这个数的字节
                continue
            print(filename)
            #是windows好像和Linux 不同在这里调了工作空间 还是要这样拼路径出来
            a=os.path.join(foldername, filename)
            print(a)
            os.unlink(a) 
            #确定要了之后  打开上面的注释 删除文件
            #Commented out to protect against accidental deletion
            print('Deleting ' + filename + '...') #Print only to verify working correctly

deleteUnneeded('e:\\n')
print('Done完成')
