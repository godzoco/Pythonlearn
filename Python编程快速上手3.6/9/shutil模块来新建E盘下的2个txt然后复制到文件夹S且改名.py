#组织文件 来处理这些文件

#shutil模块来提供函数，用于复制文件和整个文件夹


import shutil,os
#进入工作目录 E盘根目录
os.chdir('e:\\')

#新建文件s29.txt
s1=open('s19.txt','w')
sfile=open('e:\\s29.txt','w')

sfile.write('hello!!!')
sfile.close()
#感谢刘嗣林的close  提醒

#新建文件夹s 这是BUG写法
#这里有一个BUG FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 's'
'''
a='s'
os.mkdir(a)
'''
#新建文件夹s 这是有s了 就跳过
a='s'
try:
    os.mkdir(a)
except OSError:
    pass


#文件夹存在就不运行了
#拷贝S29到S里面
shutil.copy('e:\\s29.txt','e:\\s')
#这样调用了 新的位置 修改了名字
shutil.copy('e:\\s29.txt','e:\\s\\s30.txt')



