# Find  outputs
class  Rat:
	def   __init__(self , nr1 = 22, dr1 = 7):  #   Constructor  with  default  values  22  and  7
		self . nr = nr1  #  Adds  variable  nr  to  object  self  with  value  nr1
		self . dr = dr1  #  Adds  variable  dr  to  object  self  with  value  nr1
	def   __str__(self):
		return  F'{self . nr}  /  {self . dr}'
#end  of  the  class
a = Rat()  #  Constructor  initializes  object  with  nr = 22 , dr = 7
b = Rat(9)  #  Constructor  initializes  object  with  nr = 9 , dr = 7
c = Rat(5,  8) #  Constructor  initializes  object  with  nr = 5 , dr = 8
d = Rat(dr1 = 9) #  Constructor  initializes  object  with  nr = 22 , dr = 9
e = Rat(dr1 = 3 , nr1 = 2) #  Constructor  initializes  object  with  nr = 2 , dr = 3
x = eval(input('Enter numerator  :  '))  #  Assume  that  input  is   11
y = eval(input('Enter Denominator  :  '))    #  Assume  that  input  is    15
f = Rat(x , y) #  Constructor  initializes  object  with  nr = user  input  'x'  , dr =  user  input  'y'
print('a  :  ' , a) #   __str__()  method  of  Rat  class  returns  '22 / 7'
print('b  :  ' , b) #   __str__()  method  of  Rat  class  returns  '9 / 7'
print('c  :  ' , c)  #   __str__()  method  of  Rat  class  returns  '5 / 8'
print('d  :  ' , d)   #   __str__()  method  of  Rat  class  returns  '22 / 9'
print('e  :  ' , e)  #   __str__()  method  of  Rat  class  returns  '2 / 3'
print('f  :  ' , f)  #   __str__()  method  of  Rat  class  returns  'x / y'
c . __init__()  #  Constructor  modifies  object  'c'  with  nr = 22 , dr = 7
print('c  :  ' , c)   #   __str__()  method  of  Rat  class  returns  '22 / 7'
e . __init__(3.8  , 4.6)  #  Constructor  modifies  object  with  nr = 3.8 , dr = 4.6
print('e  :  ' , e)    #   __str__()  method  of  Rat  class  returns  '3.8 / 4.6'
#g = Rat(nr1 = 9 , 5) # Error :  Cannot  pass  positional  argument  5  after  keyword  argument  nr1 = 9
#h = Rat(nr = 9 , dr = 5)  # Error :  Constructor  does  not  have  args  nr  and  dr


'''
Object  'a'   --->  nr = 3.8 , dr = 4.6

Object  'b'   --->  nr = 9 , dr = 7

Object  'c'   --->  nr = 22 , dr = 7

Object  'd'   ---> nr = 22 , dr = 9  

Object  'e'   --->  nr = 2 , dr = 3

Object  'f'   --->  nr = 11 , dr = 15


1) What is  the  advantage  with  default  arguments  for  constructor ?  --->
																										Can  create  object  with  0 , 1  (or)  2  arguments
																										Eg: rat()  , rat(5)  and  rat(5 , 8)  are  valid
																										      due  to  default  arguments

2) What  is  the  issue  without  default  arguements  ?  --->  Can  create  object  with  two  arguments  only
																								Eg:  rat(5 , 8)

3) In  other  words,  rat()  and  rat(5)  raises  error  when  default  values  are  missing

4) Can  argument  and  instance  variable  have  same  name ?  --->  Yes  but  not  recommended

5) How  are  they  distinguished  when  they  have  same  name ?  --->
																									Instance  variables  are  denoted  by  self . nr , self . dr
																		                            and  parameters  are  denoted  by  nr , dr
																									Eg:  def   __init__(self , nr = 22 , dr = 7):
																																self . nr = nr
																																self . dr = nr
'''
