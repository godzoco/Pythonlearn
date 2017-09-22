
path1 = 'C:\kms10.log'
#with open(path1) as file_object:
c = open(path1).read() 
#c = file_object.read()
print(c.rstrip())