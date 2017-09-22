import re
import pyperclip
#phoneRegex=re.compile(r'\d{3}-\d{8}|\d{4}-\{7,8}')
#emailRegex=re.compile(r'\w[-\w.+]*@([A-Za-z0-9][-A-Za-z0-9]+\.)+[A-Za-z]{2,14}')

#test=phoneRegex.search('027-83885997')
#print(test.group())
"""
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?    #area code
    (\s|-|\.)?            #seperator
    (\d{3})               #first three digits
    (\s|-|\.)             #seperator
    (\d{4})               #last four digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    #extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+    #username
    @                    #symbol
    [a-zA-Z0-9.-]+       q#domain name
    (\.[a-zA-Z]{2.4})    #dot something
    )''', re.VERBOSE)


text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])
    
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
"""