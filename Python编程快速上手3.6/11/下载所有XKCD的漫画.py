#!/usr/bin/env python3

#Chapter 11 Project
#XKCD Comic Download - Downloads every XKCD comic

import requests
import os
import bs4

#要做到的事情
'''
1用request 模块下载页面
2Beautifulsoup 找到图片的中的URL
3iter_content()下载漫画图像，存硬盘
4找前面的的漫画连接然后重复，保存为downloadXKCD.py
'''
url = 'http://xkcd.com' #Starting url
os.makedirs('xkcd', exist_ok=True)  #Store comics in ./xkcd#新建一个保存图片的目录 exist_ok=True确保这个文件夹存在
#1发现 图形的<IMG> 元素 都在 <div id ="comic">
while not url.endswith('#'):
    #Download the page URL 以#结束 就停止循环
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()#不成功下载就抛出异常，

    soup = bs4.BeautifulSoup(res.text)#用下载页面的文本造一个BeautifulSoup对象
    comicElem = soup.select('#comic img') #根据 这个网站 图片 在 comic  这个DIV中
    if comicElem == []:
        print('Could not find the comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image 如果找到了 连接 取得这个连接的SRC 传给requests.get（）下载
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)#循环处理 iter_content()方法的返回值，将图像写入文件，最多10万字节，然后关闭
        imageFile.close()

    #Get the Prev button's url.# 这个是前一页的按钮 PREV <a> 的这个元素 用这个HREF 找到前一张图片的URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')

print('Done.')
