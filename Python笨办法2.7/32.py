#coding=utf8
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

#这里让这e 新建一个空表

#再使用range 设置从0 到6
#这里得到的值 就是从0 1 2 3 4 5
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
    #print "Adding %d 这个打印可以没有 就显示过程 
    #这里正在加人元素到表 里的 是elements.append(i)
    #append（） 函数加人元素到表
    
    #d 整形  %s 字符型  %r 混合型
    

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
 

