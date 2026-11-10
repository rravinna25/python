# Find  outputs
class  Test:
	def  __init__(self):  #  self  is  object  't'
		self . x = 10 #  Adds  public  variable  'x'  to  object  self  with  value  10
		self . __y = 20 # Adds  private  variable  'y'  to  object  self  with  value  20
	def  m1(self):  #  self  is  object  't'
		print('m1  method')
		print(self . x) #  public  variable  i.e. 10
		print(self . __y) #  private  variable  i.e.  20
		self . __m2() #  Executes  private  method  of  same  class
		print('Back to m1 method')
	def  __m2(self):  #  self  is  object  't'
		print('__m2  method')
		print(self . x) #  public  variable  i.e. 10
		print(self . __y) # private  variable  i.e. 20
# End  of  the  class
t = Test() #  Constuctor  initializes  object  with  x = 10 , __y = 20
print('Outside') # Outside
print(t . x) #  public  variable  i.e. 10
print(t . _Test__y)  # private  variable  indirectly  i.e. 20
#print(t . __y) # Error :  Cannot  use  private variable  __y  outside  the  class  becoz  it  is  not  visible
print(t . __dict__) # {'x' : 10 , '_Test__y' : 20}
t . m1() #  Executes  method  m1()  of  Test  class
t . _Test__m2() # Executes  private  method  m2()  of  Test  class  indirectly
#t . __m2() # Error :  Cannot  call  private method  __m2()  outside   the  class  becoz  it  is  not  visible
print('End') # End


'''
Outside
10
20
{'x':10,'_Test__y':20}
m1 method
10
20
__m2 method
10
20
Back to m1 method
__m2 method
10
20
End


1) How  to  use  private  variable  outside  the  class  ?  --->  object . _classname__variablename

2) How  to  use  private  variable  in  methods  of  same  class  ?  --->  object . __variablename

3) How  to  call   private  method  outside  the  class  ?  --->  object . _classname__method()

4) How  to  call   private  method  in  methods  of  same  class  ?  --->  object . __method()
'''
