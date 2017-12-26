
#webbrowser模块的open() 可以打开新的浏览器 打开指定的url

#The Adventures of Tom Sawyer by Mark Twain
#x下载 这把书
#http://www.gutenberg.org/ebooks/74
#txt版本的地址http://www.gutenberg.org/files/74/74-0.txt
# requests 是要先PIP INSTALL REQUESTS 先安装才有

import requests

res = requests.get('http://www.gutenberg.org/files/74/74-0.txt')
try:
    res.raise_for_status()
except Exception as exc:
    print('有问题:%$'%(exc))

playfile = open ('The Adventures of Tom Sawyer by Mark Twain.txt','wb')
for chunk in res.iter_content(10000):
    playfile.write(chunk)

playfile.close()