path1 = 'a/pi_30_digits.txt'
#path1 = 'a/3.14.txt'

with open(path1) as fl:
    c1 = fl.readlines()
pi=''
for line in c1:
    pi += line.strip()
print(pi)
print(len(pi))