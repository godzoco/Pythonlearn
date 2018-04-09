#!/usr/bin/env python

import os, sys
import filecmp
import re
import shutil
holderlist=[]

def compareme(dir1, dir2):
    dircomp=filecmp.dircmp(dir1,dir2)#查API 就是上文的目录比较.dircmp(dir1,dir2)
    only_in_one=dircomp.left_only #左目录只在左目录的文件或者目录 源文件的新文件或者目录
    diff_in_one=dircomp.diff_files #不匹配的文件
    dirpath=os.path.abspath(dir1)#返回path规范化的绝对路径 如果有新文件就更新 加入下面的数组
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in only_in_one]
    [holderlist.append(os.path.abspath( os.path.join(dir1,x) )) for x in diff_in_one]
    #上面合并好路径，一起新的文件和目录 再作绝对路径 循环X个不同文件和目录加入 列表
    if len(dircomp.common_dirs) > 0:#判断有没有 相同子目录
        for item in dircomp.common_dirs:# 相同子目录如果有就按这么 循环找下去
            compareme(os.path.abspath(os.path.join(dir1,item)), \
            os.path.abspath(os.path.join(dir2,item)))
        return holderlist#最后得到差异的列表

def main(): #从这里开始
    if len(sys.argv) > 2:#要求输入源目录和备份目录
        dir1=sys.argv[1]
        dir2=sys.argv[2]
    else:
        print("Usage: ", sys.argv[0], "datadir backupdir")
        sys.exit()

    source_files=compareme(dir1,dir2)
    dir1=os.path.abspath(dir1)

    if not dir2.endswith('/'): dir2=dir2+'/'#备份目录没有加/ 就加/ 结尾
    dir2=os.path.abspath(dir2)
    destination_files=[]
    createdir_bool=False

    for item in source_files:
        destination_dir=re.sub(dir1, dir2, item)#两个路径下的差异的目录和文件
        destination_files.append(destination_dir)
        if os.path.isdir(item):#如果差异为路径且不存在，则在备份中创建
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
                createdir_bool=True

    if createdir_bool:#如果新生成的目录好了，再调用一次对比遍历
        destination_files=[]
        source_files=[]
        source_files=compareme(dir1,dir2)
        for item in source_files:
            destination_dir=re.sub(dir1, dir2, item)
            destination_files.append(destination_dir)

    print("update item:")
    print(source_files)

    copy_pair=zip(source_files,destination_files)#这里S是源的目录 D是差异的文件
    for item in copy_pair:
        if os.path.isfile(item[0]):
            shutil.copyfile(item[0], item[1])#

if __name__ == '__main__':
    main()
#所以其实在代码中使用 if __name__ == '__main__',
    # 相当于使用一个if判断，在此if条件下的内容不会在被引入模块的文件中调用，
    # 因为不是在当前py文件中直接调用，__name__会等于被引模块的文件名。
