# Find outputs  (Home  work)
from  mod1  import  * #  Imports  object  'x' , function  f1()  and  class  c1  of  mod1
from  mod2  import  * #  Imports  object  'x' , function  f1()  and  class  c1  of  mod2
x = 30
def   disp():
	print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
print(x) #  Object  'x'  of  current  module  i.e.  30
disp() #   Executes  disp()  function  of  current  module
a = c1()  #  Creates  c1  class  object  of  current  module
a . m1() # Executes   method   m1()  of  class  c1  in  current  module


'''
30
disp  function  of  same  module
m1  method of  class  c1  in  same  module
'''
