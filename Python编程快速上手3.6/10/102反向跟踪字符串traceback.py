#Python 执行错误时，会生成错误信息，称为'反向跟踪'
#包含了  错误调用的序列，这个序列称为"调用栈"
import traceback,os
os.chdir('e:\\')
try:
    raise Exception('这是个错误信息')
except:
    errFile = open('errinfo.txt','w')
    errFile.write(traceback.format_exc())
    errFile.close()
    print('写入异常信息到errinfo.txt')              
#这个错误 发生在第 5行 