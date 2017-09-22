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
    print('1222第一个调整去除后面的空\n'+stringrem) 
    stringrem = fspaceRegex.sub('', stringrem)
    return stringrem

remspace('    here is the string    ')
print(stringrem)