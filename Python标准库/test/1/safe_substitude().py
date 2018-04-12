import string  
  
values = {'var' : 'foo'}  
  
#t = string.Template('''$var is here but  missing is not provided! ''')
t = string.Template("""
Variable        : $var
Escape          : $$
Variable in text: ${var}iable
""")
  
##    print 'substitute() : ', t.substitute(values)
#except ValueError as err:
 #   print 'Error:', str(err)
print('substitude() : ', t.substitute(values))
#print('safe_substitude() : ', t.safe_substitute(values))
