def p(u,c):
    while u:
        x=u.pop()
        print("我"+x)
        c.append(x)
def s(c):
    print("第二")
    for cac in c:
        print(cac)
u=["dasd","sad","212dasd"]
c=[]
p(u,c)
s(c)