#webbrowser模块的open() 可以打开新的浏览器 打开指定的url

#beautifulsoup 模块要 pip install beautifulsoup 加入进去
import hashlib
import bs4
import webbrowser
import requests
#res= requests.get('https://www.nostarch.com/')
es = requests.get('https://www.baidu.com/')

#res= requests.get('http://www.nostarch.com/')


es.raise_for_status()
#tar = bs4.BeautifulSoup(res.text)

ex = open('ex.html')
#exsoup = bs4.BeautifulSoup(ex)

ess = bs4.BeautifulSoup([ex], "html.parser")

