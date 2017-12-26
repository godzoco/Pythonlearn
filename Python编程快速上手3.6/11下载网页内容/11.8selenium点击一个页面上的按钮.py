#webbrowser模块的open() 可以打开新的浏览器 打开指定的url

from selenium import webdriver

b= webdriver.firebox()
b.get('http://inventwithpython.com/')
l = b.find_elemnet_by_link_text('Read It Online')

l.click()