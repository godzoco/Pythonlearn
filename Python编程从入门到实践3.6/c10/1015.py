path1 = 'a/a12.txt'
#path1 = 'a/kms10.log'
with open(path1) as fl:
    c1 = fl.readlines()
pi=''
for line in c1:
    pi += line.rstrip()
print(pi)
print(len(pi))