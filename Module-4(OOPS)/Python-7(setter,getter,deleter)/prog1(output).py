# getter  and  setter  methods  demo  program
class  Celsius:
	def   __init__(self , x):
		self . temp = x  #  Executes  setter  method   as  instance variable  is  initialized
	'''
	@property
	def  temp(self):  #  self  is  object  'a'
		print('Getter  method')
		return  self . _temp  #  Returns  backup   variable
	'''		
	@temp . setter
	def   temp(self ,  y):
		print('Setter  method')
		if  y  <  -273.15:
			raise  ValueError('Temperature  below  -273  is  not  possible')
		self . _temp =  y   #  Adds   2nd  variable  _temp  to  object   'a'  with  value  37
	def   convert(self):  #  self  is  object  'a'
		return   1.8 * self . temp  +  32 #   getter  method  returns   37
#End  of  the  class
try:
	a  =  Celsius(37)  #  Constructor  and   setter  method  initializes  object  with  temp = 37  , _temp = 37
	print(a . temp) #   getter  method  returns   37
	print('Farenheit  eqv  :  ' , a . convert())
	b  =  Celsius(-300)   #  Constructor  initializes  object  with  temp =  -300  and  setter   method  raises  an  error
	print('Hello')  # Skipped  due to  error
except  ValueError  as  msg: #  msg  is  Temperature  below  -273  is  not  possible
	print(msg)
print('End')


'''
Setter  method
Getter  method
37
Getter  method
Farenheit  eqv :  98.6
Setter  method
Temperature  below  -273  is  not  possible
End


Object  'a'   --->   temp = 37 , _temp = 37

Object  'b'  --->     temp = -300


1) What  is  the  issue  with  return  self . temp  in  getter  method ?  --->	Executes  same  getter  method  which  leads  to  recursion

2) What  is  the  issue  without  return  statement  in  getter  method ?  --->  None  is  returned  by  default

3) Where  is  None  returned  to  ?  --->  obj . temp

4) Hence  getter  method  has  to  return  2nd  variable  _temp  i.e.  Bakcup  variable

5) What  is  the  issue  without  self . _temp = x  in  setter  method ? --->																			
											getter  method  raises  error  becoz  object  self  does  not  have  variable  _temp 

6) Hence  self . _temp = x  is  mandatory  in  setter  in  view  of  getter  method

7) What  is  the  issue  with  self . temp = x  in  setter  method ?  --->																																									
																					Executes  same  setter  method  which  leads  to  recursion

8) What  does  a . temp = 37  do ?  --->  Assigns  37  to  a . temp  and  a . _temp  due  to  setter  method
'''
