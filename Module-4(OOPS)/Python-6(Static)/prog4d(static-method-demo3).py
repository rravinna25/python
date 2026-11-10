#  Find  outputs
class   c1:
	@staticmethod
	def   m1(self):
		print(self)
#  End  of  the   class
c1 . m1(25)  #  Executes  static  method  of  class  c1  and  self  is   25
a = c1() #  Empty object
a . m1(35)  #  Executes  static  method  of  class  c1  becoz  'a'  is  c1  class  object  and  self  is   35
#a . m1()  # Error : method  expects  an  argument  but  nothing  is  passed


'''
1) Is  m1()  a  static  method ?  --->  Yes  becoz  it  has  the  decorator  @staticmethod

2) How  many  arguments  can  a  static  method  have ?  --->  0 , 1  (or)  more  than  one

3) Can  static  method  be  called  wrt  object ?  ---> Yes  but  not  recommended
'''
