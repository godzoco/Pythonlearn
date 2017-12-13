#Python 执行错误时，会生成错误信息，称为'反向跟踪'
#包含了  错误调用的序列，这个序列称为"调用栈"


def spam():
    bacon()
def bacon():
    raise Exception('这是个错误信息')

spam()

#这个错误 发生在第 5行 