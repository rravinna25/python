# Tricky  program   (Home  work)
# What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40 , 50 , 60 , 70
class   Test:
	@classmethod
	def  get1(cls):
		cls . x = int(input('Enter  any  number    :  '))  #  Adds  static  variable  'x'  to  class  c1  with  user  input  10
	def  get2(self):
		self . y = int(input('Enter  any  number  :  ')) # Adds  instance  variable  'y'  to  object  self   with  user  input
		self . z = int(input('Enter  any  number  :  '))  # Adds  instance  variable  'z'  to  object  self   with  user  input
	def   compute(self):
		Test . x += 1  #  Increments  static  variable  'x'  of  class  c1  by  1
		self . y  += 1   #  Increments  instance  variable  'y'  of  object  self  by  1
		self . z  += 1  #  Increments  instance  variable  'z'  of  object  self  by  1
		self . x  += 1  #  self . x = self . x + 1 --->  # Adds  instance  variable  'x'  to  object  self   with  the  result
	def    disp(self):
		print(Test . x , self . y , self . z ,  self . x , sep = '\t')
# End  of  the  class
Test . get1()  # Executes  class   method  of  Test  class
a = Test()  # Three  empty  Test  class  objects
b = Test()
c = Test()
a . get2() #  Reads  inputs  to  object  'a'
b . get2()  #  Reads  inputs  to  object  'b'
c . get2()  #  Reads  inputs  to  object  'c'
a . compute()
b . compute()
c . compute()
a . disp()  #  13      21      31     12
b . disp()  #  13      41      51     13
c . disp()  #  13      61      71     14



'''
static   variable   --->  x = 13

Object  'a'  --->  y = 21 , z = 31 , x = 12

Object  'b'  --->  y = 41 , z = 51 , x = 13

Object  'c'  --->  y = 61 , z = 71 , x = 14
'''
