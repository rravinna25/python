#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):  #  Deleted  becoz  it  does  not  have  reference
		print('static  method')
		print(self)
	def   m1(self): #  Alive :  It  has  got  reference  m1
		print('instance  method')
		print(self)
#  End  of  the   class
c1 . m1(25) #  Executes  method  of  class  c1  and  self  is  25
a = c1()   # Empty  object
a . m1()  #  Executes  method  of  class  c1  and  self  is  object  'a'


'''
instance  method
25
instance  method
Type  and  address  of  obejct  'a'
'''
