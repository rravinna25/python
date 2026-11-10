# Find  outputs (Home  work)
class  c1:
	x = 10  #  Adds  static  variable  'x'  to  class  c1  with  value  10
	def  m1(self):  #  self  is   object  'a'
		self . x = 20  
a = c1()  #  Empty  object
a . m1() #  Method  m1()  adds   variable  'x'  to  object  'a'  with  value  20
print(c1 . x) #  10 : static  variable  of  class  c1   
print(a . x) #  20 :  Variable  'x'  is  of  object  'a' 


'''
static   variable   --->  x = 10

object  'a'   --->  x = 20
'''
