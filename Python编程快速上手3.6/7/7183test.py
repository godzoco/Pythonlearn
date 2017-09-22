#!python3
# Chap7PracStrip
# Remove whitespace from beginning and end of string using regex

import re

def remspace(string):
    global stringrem
    print('1原来的\n'+string)
    bspaceRegex = re.compile(r'\s*$')
    fspaceRegex = re.compile(r'^\s*')
    stringrem = bspaceRegex.sub('', string)
    print('2第一个调整去除后面的空\n'+
          '3这个就是用没有字符把空字符串代替了\n'
          '4也就是先结尾用空的‘’代替，再头用‘’代替\n'
          '5先看后面，用$结束，用‘’直接替换了结束末尾的空格\n'+stringrem) 
    stringrem = fspaceRegex.sub('', stringrem)
    return stringrem

remspace('    here is the string    ')
print(stringrem)