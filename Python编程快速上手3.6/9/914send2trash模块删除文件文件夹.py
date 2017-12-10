

import send2trash,os
os.chdir('d:\\')


b=open('s1.txt','a')
b.write('hello')
b.close()

send2trash.send2trash('s1.txt')
#
#这样在D这个根目录 新建了文件
#然后马上用send2 删除 再去 回收站可以找到文件恢复
 