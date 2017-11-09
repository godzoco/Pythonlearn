import shelve
sfile=shelve.open('mydata')
cat=['a','b','c']
sfile['cats']=cat
sfile.close()

sfile=shelve.open('mydata')
print(type(sfile))

print(sfile['cats'])

print(list(sfile.keys()))
print(list(sfile.values()))


sfile.close()

