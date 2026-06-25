#  Difference  between  function   and   method
class    c1:
	def   m1(self):
		print('Method')
# End  of  the  class
def   f1():
	print('Function')
# End  of  the  function
a = c1()  #  Creates  c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  as  'a'  is  c1  class  object
f1()  #  Executes  function  f1()
a . f1() #  Error :  class  c1  does  not  have  method  f1()  
m1(a)  #  Error :  Current  module  does  not  have  function  m1()
