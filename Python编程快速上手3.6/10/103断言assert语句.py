#断言 是一个心智正常的 检查
#确保代码没有 做明显错误的事情 用assert语句

#1 assert
#2 条件  求值为true或者False
#3 逗号
#4 在条件false时显示字符串


pod = 'open'
assert pod == 'open','the pod 需要是open状态'
pdp = '可能不是open状态'
#assert pod == 'open','the pod 需要是open状态'
assert pod == 'open1','the pod 需要是open状态'

#断言是open 如果改成open1 就有错误

#这样断言 就会抓住这个 错误  就是找到程序员 看错或者写错

#比如交通灯 的问题 ，设置了一个断言 之后 ，就可以快速找到 出错的问题 ，然后解决