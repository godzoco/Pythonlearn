
path1 = 'a/kms10.log'
with open(path1) as fl:
    c1 = fl.readlines()
for line in c1:
    print(line.rstrip())