#  dir()  function  demo  program  (Home  work)
from  prog10a   import  rat #  imports  rat  class  and  if  statement  outside  rat  class  of  prog10a
a = rat()  #  Creates  an  empty  rat  class  object
a . nr = 22  #   Adds  variable  nr  to  object  'a'  with  value   22
a . dr = 7  #   Adds  variable  dr  to  object  'a'  with  value   7
print(dir(rat))  #  All  the  method  of  rat  class  i.e.  ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '__str__']
print()
print()
print(dir(a))   #  All  the   variables  of  object  'a'  and  method  of  rat  class  i.e.  ['nr' , 'dr' , 'add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '__str__']#   ['add', 'div', 'get', 'mul', 'simplify', 'sub', 'test' , '__str__']



# object  'a'  ---> nr = 22 , dr = 7
