'''  (Home  work)
Write  a  program  to  add  two  objects  where  each  object  contains  three  values  and
store  results  in   third  object

1st  object   --->  x = 10 , y = 20 , z = 30

2nd  object --->  x = 40 , y = 50 , z = 60

3rd  object  ---> x = 10 + 40 = 50 , y = 20 + 50 = 70 , z = 30 + 60 = 90
'''
class  Test:
	def   get(self):
		 self . x = eval(input('Enter  1st  number  :  '))  #  Adds  variable  'x'  to  object  self  with  user  input
		 self . y = eval(input('Enter  2nd  number  :  ')) #  Adds  variable  'y'  to  object  self  with  user  input
		 self . z = eval(input('Enter  3rd  number  :  '))  #  Adds  variable  'z'  to  object  self  with  user  input
	def   add(self , m , n):  #   self  is  object  'c' , 'm'  is  object  'a'  ,  'n'  is  object  'b'
		 self . x = m . x + n . x  #  Adds  variable  'x'  to  object  self   with  the  result
		 self . y = m . y + n . y  #  Adds  variable  'y'  to  object  self   with  the  result
		 self .  z = m . z + n . z  #  Adds  variable  'z'  to  object  self   with  the  result
	def  disp(self):  #   self  is  object  'c'
		 print('x : ' , self . x)  #  prints  c . x
		 print('y : ' , self . y)   #  prints  c . y
		 print('z : ' , self . z)   #  prints  c . z
# End  of  the  class
a = Test() #  Create  three  empty  Test  class  objects
b = Test()
c = Test()
print('First  Object')
a . get() #  Reads  inputs  to  object  'a'
print('Second  Object')
b . get() #  Reads  inputs  to  object  'b'
c . add(a , b) # Adds   objects  a  and  b  and  stores  results  in  object  'c'
print('Addition  results')
c . disp() #  Prints  values  of  object  'c'


'''
object  'a'  --->   x = 10 , y = 20 , z = 30

object  'b'  --->   x == 40 , y = 50 , z = 60

object  'c'  --->   x = 50 , y = 70 , z = 90


1) Is  c = a + b  valid ?   --->  No  becoz   Test  class  does  not  have   __add__()  method 

2) What  does  print(c)  do ?  --->  Executes  __str__()  method  of  object  class  becoz  Test  class  does  not  have 
													  __str__()  method

3) What  does  __str__()  method  of  object  class  do ?  --->  Returns  type  and  address  of  object  'c'
'''
