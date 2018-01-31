from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import sys


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        #bsObj = BeautifulSoup(html.read())这是原代码原书代码，现在应该更新了
        title = bsObj.body.h1
        #title = bsObj.body.h100000
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
#title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html1")

if title == None:
    print("Title could not be found")
else:
    print(title)

