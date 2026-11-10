
'''
Write  a  program  to  add , subtract , multiply  and  divide  two  rational  numbers

1) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   5 / 9
    What  is  the  sum  ?  --->  2 / 3 + 5 / 9 =  (18 + 15) / 27 =  33 / 27 =  11 / 9
    What  is  the  difference  ?  ---> 2 / 3 - 5 / 9 = (18 - 15) / 27 = 	3 / 27 = 1 / 9
    What  is  the  product  ?  --->  2 / 3 * 5 / 9 =	10 / 27  = 10 / 27
    What  is   the  division  ?  --->  2 / 3 /  5 / 9 =  2 / 3 * 9 / 5 =  18 / 15 =  6 / 5  --->  Succesful  division  and   return  True

2) 1st  rational  number  --->  2 / 3
    2nd  rational  number  --->   0 / 9
    What  is  the  sum  ?  --->  2 / 3 + 0 / 9 = (18 + 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  difference  ?  ---> 2 / 3 - 0 / 9 = (18 - 0) / 27 =  18 / 27 = 2 / 3
    What  is  the  product  ?  --->  2 / 3 * 0 / 9 =	0 / 27  =  0 / 27  --->  Simplification  is  not  required  becoz  numerator  is  0
    What  is   the  division  ?  --->   2 / 3 /  0 / 9 =  2 / 3 * 9 / 0 =  18 / 0  ---> Division  is  not   permitted  and  return  False

3) When  is  simplification  required ?  ---> When  numerator  is  non-zero

4) What  does  div()  method  return ?  ---> True  when  division  is  succesful  and  False  otherwise
'''
import  math
class  rat:
	def  get(self):
		self . nr = int(input('Enter  numerator :  '))  # Adds  variable  nr  to  object  self  with  user  input
		self . dr = int(input('Enter  denominator :  '))  # Adds  variable  dr  to  object  self  with  user  input
		self . test()  #  Is  denom  of  object  self  zero
	def  test(self):
		while  self . dr == 0:  #  Execute  until  dr  is  non-zero
			self . dr = int(input('Denom  can  not  be  zero , reenter :  '))  #  Reads  non-zero  denominator  to  object  self
	def    __str__(self):
			 return  F'{self . nr} / {self . dr}'  #   Concatenates  values  of  self  to  form  a  string  with  '/'
	def   add(self , a , b):
		self . nr = a . nr * b . dr + a . dr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr  # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()  #  Simplifies  values  of  object  self
	'''
	c . add(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  c  --->  2 / 3 + 5 / 9 = (2 * 9 + 5 * 3) / (5 * 9) = 33 / 27 = 11 / 9
	'''
	def   sub(self , a , b):
		self . nr = a . nr * b . dr - a . dr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr   # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()   #  Simplifies  values  of  object  self
	'''
	d . sub(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  d  --->  2 / 3 - 5 / 9 = (2 * 9 - 5 * 3) / (5 * 9) = 3 / 27 = 1 / 9
	'''
	def   mul(self , a , b):
		self . nr = a . nr * b . nr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . dr   # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()   #  Simplifies  values  of  object  self
	'''
	e . mul(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  e  --->  2 / 3 * 5 / 9 = (2 * 5) / (3 * 9) = 10 / 27
	'''
	def    div(self , a , b):
		self . nr = a . nr * b . dr  # Adds  variable  nr  to  object  self  with  the  result
		self . dr = a . dr * b . nr  # Adds  variable  dr  to  object  self  with  the  result
		self . simplify()  #  Simplifies  values  of  object  self
	'''
	f . div(a , b)
	object  a  --->  2 / 3
	object  b  --->  5 / 9
	object  f  --->  2 / 3 / 5 / 9 = 2 / 3 * 9 / 5 = (2 * 9) / (3 * 5) = 18 / 15 = 6 / 5
	'''
	def   simplify(self):
		if  self . nr != 0:
			ans = math . gcd(self . nr , self . dr)  #  gcd  of  values  of  self
			self . nr = self . nr // ans  #  Simplifies  nr  of  object  self
			self . dr = self . dr // ans   #  Simplifies  dr  of  object  self
	'''
	c . simplify()
	1)  12 / 15  --->  4 / 5
	2) 10 / 27   --->  10 / 27
	3) 0 / 27  --->   0 / 27
	'''
# End  of the class
if  __name__  == '__main__':
	a = rat() #  Creates  6  empty  rat  class  objects
	b = rat()
	c = rat()
	d = rat()
	e = rat()
	f = rat()
	a . get()  #  Reads  inputs  to  object  'a'
	b . get()  #  Reads  inputs  to  object  'b'
	c . add(a , b)  #  Adds  objects  'a'  and  'b'  and  stores  results  in  object  'c'
	d . sub(a , b)  #  Subtracts  objects  'a'  and  'b'  and  stores  results  in  object  'd'
	e . mul(a , b)  #  Multipliees  objects  'a'  and  'b'  and  stores  results  in  object  'd'
	print('Sum : ' , c)  #   __str__()  method  of  rat  class  returns   values  of  object  'c'  in  the  form  of  string
	print('Difference : ' , d)  #   __str__()  method  of  rat  class  returns   values  of  object  'd'  in  the  form  of  string
	print('Product : ' , e)  #   __str__()  method  of  rat  class  returns   values  of  object  'e'  in  the  form  of  string
	if  b . nr != 0:
		f . div(a , b)  #  Divides  objects  'a'  and  'b'  and  stores  results  in  object  'f'
		print('Division : ' , f)  #   __str__()  method  of  rat  class  returns   values  of  object  'f'  in  the  form  of  string
	else:
		print('Division  is  not  permitted')


'''
Object  'a'  --->  nr = 2 , dr = 3

Object  'b'  --->  nr = 5 , dr = 9

Object  'c'  --->  nr = 11 , dr = 9

Object  'd'  --->  nr = 1 , dr = 9

Object  'e'  --->  nr = 10 , dr = 27

Object  'f'  --->  nr = 6 , dr = 5



1) Can  a  method  call  another  method  of  same  class ?  --->  Yes  with  self . method()

2) get()  calls  which  method  ?  ---> Method  test()  of  the  same  class

3) If  get()  method  is  called  wrt  obj  'a' ,
    test()  method  is  called  wrt  which  object ?  --->  Same  object  'a'  due  to  self . test()

4) add()  calls  which  method  ?  --->  Method  simplify()  of  the  same  class

5) If  add()  method  is  called  wrt  object  'c',
    simplify()  method  is  called  wrt  which  object ?  --->  Same  object  'c'  due  to  self . simplify()

6) In  which  order  can  methods  of  the  class  can  be  defined ?  ---> Any  order

7) Can  a  method  be  called  before  it  is  defined ?  ---> Yes
    Can  a  function  be  called  before  it  is  defined ?  ---> 
																Yes  when  a  method  (or)  function  calls  it  and  no  when  it  is  called  outside
'''
