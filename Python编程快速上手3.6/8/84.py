import pprint
cats=[{'name':'z','desc':'zd'},{'name':'f','desc':'fd'}]
print(pprint.pformat(cats))

pprint.pformat(cats)

file=open('mycat.py','w')
file.write('cat ='+pprint.pformat(cats)+'\n')
file.close()
