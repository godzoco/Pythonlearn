import zipfile,os
os.chdir('e:\\')

#工作目录      使用以下代码，必须先生成一个e.zip的文件，sp.txt在e根目录下
#而且设定 D的盘下面有一个ZIP的文件e.zip
#然后一个文件夹c和sp.txt
#再c文件夹中有ca.txt和zo.txt

#['e/', 'e/c/', 'e/c/ca.txt', 'e/c/zo.txt', 'e/sp.txt'] 这个是目录
ex=zipfile.ZipFile('n.zip')
#调ZIP对象 以下的是解压缩extractall()
ex.extractall()
#ex.close()

#然后用extract()传递字符串  得到解压缩出来的文件
ex.extract('n/sp.txt','e:\\2')
#这里extrac() 半天没弄好 这个直接 不要用这个close就好了
#ex.close()

#感谢刘嗣林