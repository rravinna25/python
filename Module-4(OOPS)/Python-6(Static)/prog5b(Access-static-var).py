# How  to  use  static  variable  in  different  ways  ?
class   c1:
	x = 25   #  Adds  static  variable  'x'  to  class  c1  with  value25
	def   __init__(self):   # self  is object  'a'
		print(c1 . x) #  25 : Static  variable  'x'  of  class  c1  
		print(self . x) #  25 : Static  variable  becoz  object  'a'  does  not  have  variable  'x' 
		#print(x) #  Error :  Local  variable   'x'  does  not  exist  in  the  constructor
	def   m1(self):  # self  is object  'a'
		print(c1 . x)  #  25 : Static  variable  'x'  of  class  c1 
		print(self . x) #  25 : Static  variable  becoz  object  'a'  does  not  have  variable  'x' 
		#print(cls . x) #  Error :  cls  does  not  exist  in  method  m1()
	@classmethod
	def   m2(cls):
		print(c1 . x) # 25 : Static  variable  'x'  of  class  c1  
		print(cls . x)  # 25 : Static  variable  'x'  of  class  c1  
		#print(self . x) #  Error : self  does  not  exist  in  method  m2()
	@staticmethod
	def   m3():
		print(c1 . x)  # 25 : Static  variable  'x'  of  class  c1  
		#print(cls . x) # cls  does  not  exist  in  method  m3()
		#print(self . x) #  Error : self  does  not  exist  in  method  m3()
# End  of  the  class
a =  c1()  #  Executes  constructor
print(c1 . x)  # 25 : static  variable  'x'  of  class  c1  i.e.  25
print(a . x)  #  25 :  static  variable  becoz  object  'a'  does  not  have  variable  'x' 
#print(x) #  Error :  Gv  'x'  does  not  exist
#print(self . x) #  Error :  self  does  not  exist  
#print(cls . x) #   Error : cls  does  not  exist
a . m1() #  Executes  method  of class  c1  becoz  'a'  is  c1  class   object
c1 . m2()   #  Executes  class  method  of class  c1
c1 . m3()   #  Executes  static  method  of class  c1
