#  Find  outputs
class  c1:
	def __init__(self):  #  self  is  object  'a'
		self . x = 10  #  Adds  public  variable  'x'  to  object  self  with  value  10
		self . __x = 20 #  Adds  private   variable  'x'  to  object  self  with  value  20
		self . __x__ = 30  #  Adds  public  dunder  variable  'x'  to  object  self  with  value  30
	def  m1(self):  #  self  is  object  'a'
		print('public method')
	def  __m1(self):  #  self  is  object  'a'
		print('private method')
	def  __m1__(self):  #  self  is  object  'a'
		print('public Dunder method')
#  End  of  the  class
a = c1()  #  Constructor  initializes  object   with  x = 10 , __x = 20 , __x__ = 30
print(a . x) #  public  variable  i.e. 10
print(a . __x__) #   public  dunder  variable  i.e.  30
print(a . _c1__x) #  20  i.e. private  variable  is  being  used  indirectly
#print(a . __x) # Error :   Can  not  use  private variable  outside  the  class  as  it  is  not  visible
a . m1() #  Executes  public  method  m1()  of  class  c1
a . __m1__() #   Executes  public  dunder  method  m1()  of  class  c1
a . _c1__m1() #  Executes  private  method  m1()  indirectly
#a . __m1() # Error :  Can  not  call  private  method  outside  the  class  as  it  is  not  visible


'''
10
30
20
public method
public Dunder method
private method


Object  'a'  --->  x = 10 , __x = 20 , __x__  = 30



1) What  is  __x  called ?  --->  private  variable  due  to  double  underscore

2) What  is   x  called ?  --->  public  variable

3) What  is  __x__  called  ?   --->  public  dunder  variable

4) What  is   __m1  called ?  --->  private  method  due  to  double  underscore

5) What  is  m1  called ?  ---> public  method

6) What  is  __m1__  called ?  ---> public  dunder  method
'''
