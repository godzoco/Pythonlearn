#!/usr/bin/env python3

#Chapter 11下载网页内容 Project
# lucky.py - Opens several Google search results

import requests
import sys
import webbrowser
import bs4

print('百度搜索...') #Display message while retrieving the Google page

res = requests.get('https://www.baidu.com/s?wd=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)
linkElems = soup.select('.r a')

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('https://www.baidu.com' + linkElems[i].get('href'))
