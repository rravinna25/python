''' (Home work)
Save  the  following  code  in    any  file  of  cwd
Find  outputs
'''
from  p1 . mod1  import  *  #  Imports  all  the  members  of  p1 . mod1  module  and  discards
from  p1 . mod2  import  *  #  Imports  all  the  members  of  p1 . mod2  module  and  discards
x = 30
def   f1():
	print('Function  of  same  module')
class  c1:
	def  m1(self):
		print('Method  of  class  c1  in same  module')
print(x) #  30 : Object  'x'   of  current  module  
f1() #   Executes  function  of  same  module
a = c1()  #  Creates  c1  class   object  of  same  module
a . m1() #  Executes  method  of  class  c1  in  same  module


'''
30
Function  of  same  module
Method  of  class  c1  in same  module
'''
