'''
Write  a  program  to  print  all  the  members  of  cal  module  without  environment  variables

1) What  is  the  result  of  '__name__' . startswith('__')  ?  ---> True

2) What  is  the  result  of  '__spec__' . endswith('__')  ?  --->  True

3) What  is  the  result  of  'spec__' . startswith('__')  ?  ---> False

4) a = []
    Append  all  the  elements  of  list  returned  by  dir()  function  to  list  'a'  except  environment  variables
'''
import cal
a = []  #  Empty  list
list = dir(cal)  #  Members  of  cal  module  i.e.  ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
for  x  in  list:  #  'x'  is  each  element  of  list
	if  not  (x . startswith('__') and x . endswith('__')):
		a . append(x)  #  Appends 'x'  to  list  'a'   if  it  is  not  environment  variable
print(a)  #  ['add', 'c1', 'div', 'mul', 'sub', 'x', 'y']
