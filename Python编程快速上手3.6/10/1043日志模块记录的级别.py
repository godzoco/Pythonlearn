import logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -%(levelname)s-%(message)s')

#日志级别
#1debug 低 2info 确定工作 3warning 可能的问题 现在不阻止程序，以后可以
#4error 记录错误失败  5critical 致命错误

logging.debug('低')
logging.info('确定工作')
logging.warning('可能的问题 现在不阻止程序，以后可以')
logging.error('记录错误失败')
logging.critical('致命错误')


#加入了 logging.disable() 就禁用了 所有消息
#ERROR  注意这路的 禁用 要注意 大写
logging.disable(logging.ERROR)
logging.error('记录错误失败')
logging.critical('致命错误！！！！！！！！！！！！！！！！！！！！')