

import shutil,os
os.chdir('d:\\')

#os.unlink(path)
#删除path地址的文件
#os.rmdir(path)
#删除path地址的文件夹 必须为空没有其他文件
#shutil.rmtree(path)
#删除path处文件夹 所有文件和文件夹都会被删除

for f in os.listdir():
    if f.endswith('.txt'):
        #os.unlink(f)
        print(f)
for a in os.listdir():
    if a.endswith('.txt'):
        os.unlink(a)
        print(a)