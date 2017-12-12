#!/usr/bin/env python3

# Chapter 9 Project Backup to Zip
# Copies a folder recursively into a zip file and names it incrementally.

import os
import zipfile

#如果不修改工作目录　就默认去这个类里面的的同级文件夹里面
#这样调整到ｅ盘
os.chdir('e:\\')
def backupToZip(folder):
    #folder = os.path.abspath(folder)
#os.path.abspath(path) #返回绝对路径
    number = 1
    while True:
        #os.path.basename(path) #返回文件名
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            #os.path.exists(path)  #路径存在则返回True,路径损坏返回False
            break
        number = number + 1
    #完成备份文件取名，先是比如bak_1 然后就是bak_2
    #相当于就 加数加到要的2上，比如1保存了。就给下面准备好了2，一有了这个2的取名就 break 走了，用实际的判断给虚名
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        #foldername　当前文件夹名字的字符串
        #subfolders 当前文件夹中子文件夹的字符串列表
        #filenames　　当前文件夹中子文件的字符串列表
        #就这三个，把这些都可以满足了
        print('Adding files in ' + foldername + '...')
        backupZip.write(foldername)
        
    
    backupZip.close()
    print('Done完成')


#backupToZip('/Users/mlotspaih/Documents/waffle')
#这个原来好像Linux的
#Window  必须要用\\  不然单斜杆＼是错的额
backupToZip('E:\\n')