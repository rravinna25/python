'''  (Home  work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
from  p1 . mod2  import  *   #  Imports  all  the  members  of  p1 . mod2  module  and  discards
from  p1 . mod1   import  *   #  Imports  all  the  members  of  p1 . mod1  module
print(x) # 10 : Object  'x'  imported  from  p1 . mod1  module  
f1() #  Executes  function  f1()  imported  from  p1 . mod1  module
a = c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  imported  from  p1 . mod1  module


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
'''
