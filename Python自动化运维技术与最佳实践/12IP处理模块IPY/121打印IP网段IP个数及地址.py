import IPy
from IPy import IP
ip = IP('192.168.0.0/16')
print(ip.len())
for x in ip:
    print(x)

