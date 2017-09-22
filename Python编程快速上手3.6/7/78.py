import re

p1=re.compile(r'\d$')
a1=p1.search('your number is 44')
print(a1)

p2=re.compile(r'\d$')
a2=p2.search('1234567890')
print(a2)

p3=re.compile(r'^\d+$')
a3=p3.search('1234567890')
print(a3)

p4=re.compile(r'Hello')
a4=p4.search('hello world')
print(a4)

