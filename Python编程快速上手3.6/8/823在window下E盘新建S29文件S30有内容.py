#在window下E盘新建S29文件S30
sfile=open('e:\\s29.txt','w')

sfile.write('hello1!!!')
sfile=open('e:\\s29.txt','r')
a=sfile.readlines()

#变成列表
print(a)

bfile=open('e:\\s30.txt','w')
b=bfile.write('hello!\n')
print(b)
bfile.close()
bfile=open('e:\\s30.txt','a')
a=bfile.write('Bacon')
