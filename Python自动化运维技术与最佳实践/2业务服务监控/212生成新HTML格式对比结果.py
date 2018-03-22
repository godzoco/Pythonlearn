import difflib
import sys
text1 =  """tex1:
 abc A
 
 
 aaaa333 1
 11111
difflib document v7.4
"""

text2 =  """tex2:
 abc a
 
 
 AAAA333B 3
 11111
difflib document v7.5
"""
text1_lines = text1.splitlines()
text2_lines = text2.splitlines()
#这个换成HTML的类
#d=difflib.Differ()
d=difflib.HtmlDiff()
#diff=d.compare(text1_lines,text2_lines)
#print('\n'.join(list(diff)))
#print(d.make_file(text1_lines,text2_lines))


f=open('HtmlDiff.html', 'w')
#print(d.make_file(text1_lines,text2_lines))
print(d.make_file(text1_lines,text2_lines),file=f)

f.close()
