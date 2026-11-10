#  Find  outputs
class   c1:
	@staticmethod
	def   m1():
		print('static  method')
#  End  of  the  class
c1 . m1() #  Executes  static  method  of  class  c1
a = c1()
a . m1()  #  Executes  static  method  of  class  c1  becoz  'a'  is  c1  class  object
#c1 . m1(25)  #  Error :  static  method  is  not  expecting  an  argument  but  argument  is  passed


'''
static  method
static  method



1) Is  m1()  a  static  method ?  --->  Yes  becoz  it  has  the  decorator  @staticmethod

2) Can  static  method  be  called  wrt  object ?  --->  Yes  but  not  recommended
'''
