import zipfile,os
os.chdir('d:\\')

#工作目录      使用以下代码，必须先生成一个e.zip的文件，sp.txt在e根目录下
#而且设定 D的盘下面有一个ZIP的文件e.zip
#然后一个文件夹c和sp.txt
#再c文件夹中有ca.txt和zo.txt

#['e/', 'e/c/', 'e/c/ca.txt', 'e/c/zo.txt', 'e/sp.txt'] 这个是目录
ex=zipfile.ZipFile('e.zip')
#调ZIP对象
a=ex.namelist()
print(a)

#如果是交互式 就直接b=ex.getinfo('sp.txt')可以了
#但是在代码里要带路径
b=ex.getinfo('e/sp.txt')
#压缩前大小
print(b.file_size)
#压缩后大小
print(b.compress_size)
#显示压缩比例
x=round(b.file_size/b.compress_size,2)
print(x)