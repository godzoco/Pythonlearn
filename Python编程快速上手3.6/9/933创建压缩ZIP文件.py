import zipfile,os
os.chdir('d:\\')
b=open('sp.txt','w')
b.write('hello!')
b.close()
#新建 一个文件写了 文件内容

#然后压缩 解压之后    这里面的内容还是有的

#但是这个SP.TXT在N的这个文件夹目录里面
n= zipfile.ZipFile('n.zip','w')
n.write('sp.txt',compress_type=zipfile.ZIP_DEFLATED)
n.close()


#如果要在这个n.zip 再加入一个文件s30
#要用 'a' 这个系数

b1=open('s30.txt','w')
b1.write('hello!')
b1.close()
m= zipfile.ZipFile('n.zip','a')
m.write('s30.txt',compress_type=zipfile.ZIP_DEFLATED)
m.close()
