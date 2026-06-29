# Find  outputs  (Home  work)
x = 30
def   disp():
		print('disp  function  of  same  module ')
class   c1:
	def   m1(self):
		print('m1  method of  class  c1  in  same  module')
from  mod2  import   *  #  Imports  object  'x' , function  f1()  and  class  c1  of  mod2
from  mod1  import   *  #  Imports  object  'x' , function  f1()  and  class  c1  of  mod1
print(x) #  Object  'x'  imported  from  mod1  i.e.  10
disp() #   Executes  disp()  function  imported  from  mod1
a = c1() #  Creates  the  last  imported   class   (i.e.  mod1 . c1)  object
a . m1() # Executes  method  of  the  imported  class  i.e. mod1 . c1


'''
10
disp  function  of  mod1
'm1  method  of  class  c1  in  mod1



Members  of  last  imported  module (i.e.  mod1)  are  used
'''
