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
a=d.make_file(text1_lines,text2_lines)
print(a,file=f)
f.close()

f1=open('HtmlDiff分析问题.html', 'w')
b=print(d.make_file(text1_lines,text2_lines))

print(b,file=f1)
f1.close()
#print只是打印给窗前看，就不需要再print(a)了
#不需要print(a,file=f)
