f='b/k1.txt'
with open(f,'w') as fl:
    fl.write('I love')
    
with open(f) as fl:    
    print(fl.read())