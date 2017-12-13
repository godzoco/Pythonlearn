#Python 执行无效代码时，就会抛出异常
# try except  

#抛出异常用rasie语句
#1 raise关键字 2 对exception函数调用 3传递给Exception 函数的字符串 包含出错信息
raise Exception('这个是错误信息') 

#如果没有 try和 except 语句来覆盖 异常的raise 语句
#程序就会崩溃  并且显示出异常的出错 信息

#一般 raise在函数中 Try和except 在调用 该函数的 代码中

