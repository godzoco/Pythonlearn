from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
webbrowser.open('http://www.pythonscraping.com/exercises/exercise1.html')

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)
print(bsObj.html.h1)
