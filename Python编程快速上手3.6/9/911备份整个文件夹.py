

import shutil,os
os.chdir('e:\\')

#新建文件夹 在工作目录下的这个S1

try:
    os.mkdir('s1')
except OSError:
    pass
sfile=open('e:\\s1\\s291.txt','w')

sfile.write('hello!!!')
sfile.close()

#复制s1的内容全部到a2 包括里面的文件
shutil.copytree('s1','a2')