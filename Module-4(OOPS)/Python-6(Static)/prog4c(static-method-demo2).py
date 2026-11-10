#  Find  outputs
class   c1:
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25) #  Executes  method  of  class  c1  and  object  25  is  passed  to  the  method
a = c1()  #  Empty  object
a . m1() #  Executes  method  of  class  c1  becoz  'a'  is  c1  class  object
#a . m1(35) #  Error :  Method  is  not  expecting  an  argument  but  arg  35  is  passed

'''
25
Type  and  address  of   object  'a'


Is  m1()  a  static  method  (or)  instance  method  ?   --->  Instance  method  becoz  it  has  argument  self
'''

object . method()
classname . method(object)
