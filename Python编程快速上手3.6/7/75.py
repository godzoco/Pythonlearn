import re
p=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=p.search('dddddddd415-555-9999   212-555-0000')
print(mo.group())

a=p.findall('dssssssssssssddd415-555-9999   212-555-0000')
print(a)

p1=re.compile(r'((\d\d\d)-(\d\d\d)-(\d\d\d\d))')
a1=p1.findall('dssssssssssssddd    415-555-9999   212-555-0000')
print(a1)

p2=re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
a2=p2.findall('dssssssssssssddd    415-555-9999   212-555-0000')
print(a2)
