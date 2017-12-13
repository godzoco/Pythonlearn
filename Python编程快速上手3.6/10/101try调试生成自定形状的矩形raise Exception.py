#Python 执行无效代码时，就会抛出异常
# try except  

#抛出异常用rasie语句
#1 raise关键字 2 对exception函数调用 3传递给Exception 函数的字符串 包含出错信息
#raise Exception('这个是错误信息') 

#如果没有 try和 except 语句来覆盖 异常的raise 语句
#程序就会崩溃  并且显示出异常的出错 信息

#一般 raise在函数中 Try和except 在调用 该函数的 代码中

#下面写一个 打印的方框

def box(symbol,width,height):
    if len(symbol) !=1:
        raise Exception('必须是一个字符，才能生成图像')
    if width <=2:
        raise Exception('宽度小于2，不能生成宽度')
    if height <=2:    
        raise Exception('高度小于2，不能生成宽度')
    print(symbol*width)
    for i in range(height-2):
        print(symbol+(' '*(width-2))+symbol)
    
    print(symbol*width)
#box('#',6,6)

for sym,w,h in (('*',4,4),('0',20,5),('X',1,3),('ZZ',3,3)):
    try:
        box(sym,w,h)
    except Exception as err:
        print("一个错误产生"+str(err))
    
















    
    