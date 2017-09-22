path1 = 'a/pi_million_digits.txt'


with open(path1) as fl:
    c1 = fl.readlines()
pi=''
for line in c1:
    pi += line.rstrip()


x=input("你生日，格式:xxxxddcc")
if x in pi:
    print("有你生日")
else:
    print("无")