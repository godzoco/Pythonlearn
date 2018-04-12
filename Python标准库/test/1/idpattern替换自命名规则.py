from string import Template
class MyTemplate(Template):
  delimiter = "#"
  idpattern = "[a][_a-z0-9]*"
def test():
  s='#aa is not #ab'
  t=MyTemplate(s)
  d={'aa':'apple','ab':'banbana'}
  print(t.substitute(d))
if __name__=='__main__':
  test()
