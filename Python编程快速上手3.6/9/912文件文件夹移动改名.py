

import shutil,os
os.chdir('d:\\')

#新建文件夹 在工作目录下的这个S1
try:
    os.mkdir('s912')
except OSError:
    pass


sfile=open('s912.txt','w')

sfile.write('hello!!!')
sfile.close()

#复制s1的内容全部到a2 包括里面的文件
shutil.move('s912.txt','s912')

#把一个新建好了的文件 重命名为a11111
asfile=open('d:\\e.txt','w')

asfile.write('hello!!!')
asfile.close()

shutil.move('d:\\e.txt','d:\\a1111.txt')

aesfile=open('d:\\e1.txt','w')
#如果没有文件夹然 写成这样 就变了 成无扩展名的文件e1111
aesfile.write('hello!!!')
aesfile.close()
shutil.move('d:\\e1.txt','d:\\e1111')


