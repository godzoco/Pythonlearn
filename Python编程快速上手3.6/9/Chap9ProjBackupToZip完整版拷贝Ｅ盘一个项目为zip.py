#!/usr/bin/env python3

# Chapter 9 Project Backup to Zip
# Copies a folder recursively into a zip file and names it incrementally.

import os
import zipfile

#如果不修改工作目录　就默认去这个类里面的的同级文件夹里面
#这样调整到ｅ盘
#os.chdir('e:\\')
def backupToZip(folder):
    folder = os.path.abspath(folder)
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
        #这个在循环中，把所有的子文件夹都遍历了一边
        backupZip.write(foldername)
        #把当前的文件夹写入到压缩文件夹里面
        for filename in filenames:
            #如果有多个文件格式jpg  txt　这些
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            #continue是继续上面的循环，不运行下面的   这个和路径有关
            #我的直接到Ｅ盘根目录，就不用上面的newbase 排除之前的备份了！！！
            #这样如果有新的　就把这个新进去
            backupZip.write(os.path.join(foldername, filename))
            #os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
    
    backupZip.close()
    print('Done完成')


#backupToZip('/Users/mlotspaih/Documents/waffle')
#这个原来好像Linux的
#Window  必须要用\\  不然单斜杆＼是错的额
backupToZip('E:\\n')