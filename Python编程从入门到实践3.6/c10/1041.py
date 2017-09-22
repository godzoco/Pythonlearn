import json
n=[2,3,5,7111111]
f='n.json'
with open(f,'w') as fl:
    json.dump(n, fl)