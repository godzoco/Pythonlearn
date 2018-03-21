import difflib

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

d=difflib.Differ()
diff=d.compare(text1_lines,text2_lines)
print('\n'.join(list(diff)))
