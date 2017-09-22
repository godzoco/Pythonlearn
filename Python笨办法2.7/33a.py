
i = 0
numbers = []

x = int(raw_input(">"))
#这个 要变成 保证里面输入的 整形
#就要用x= int()
#转化一波
while i < x:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
 
 
 
 

