import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -%(levelname)s-%(message)s')

#比如准备做一个 阶乘 ，然后写错了一个地方 调整 日志 查看这个问题

logging.debug('开始')

def f(n):
    logging.debug('程序开始  f(%s)' %(n))
    t= 1
    for i in range(n+1):
        #range(6)  [0,1,2,3,4,5]
        t *=i  #t=t*i
        logging.debug('i 是'+str(i)+',t是'+str(t))
    logging.debug('程序结束  f(%s)' %(n))
    return t

print(f(5))

logging.debug('结束')

#这个会弹出控制台 消息 是basicConfig() 使用的
#这里发现 不能用0开始 而是应该 1开始 才是对得  得到f(5)= 120
logging.debug('开始')

def f1(n):
    logging.debug('程序开始  f1(%s)' %(n))
    t1= 1
    for i in range(1,n+1):
        #range(1,6)  [1,2,3,4,5]
        t1 *=i #t=t*i
        logging.debug('i 是'+str(i)+',t是'+str(t1))
    logging.debug('程序结束  f1(%s)' %(n))
    return t1

print(f1(5))

logging.debug('结束')

#真正开发的时候，应该多用这种调试，print() 可能会忘记，不清除给用户看，影响不好



