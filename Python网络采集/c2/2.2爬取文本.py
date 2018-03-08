from urllib.request import urlopen
from bs4 import BeautifulSoup
import webbrowser
webbrowser.open('http://www.pythonscraping.com/pages/warandpeace.html')

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")
allText = bsObj.findAll(id="text")
print(allText[0].get_text())
