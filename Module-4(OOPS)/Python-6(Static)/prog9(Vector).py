'''
Write  a  program  to  add  two  Vector  objects

1) What  are  the  names  of  objects ?  ---> x , y   and  z

2) What  are  the  names  of   lists  held  by  each  object ?  --->  x .  a , y . a  , z . a

3) How  to  access  elements  of  1st  list ?  ---> x . a[i]
    How  to  access  elements  of  2nd  list ?  ---> y . a[i]

4) How  to  access  static  variable  'n' ?  ---> vector . n
'''
class  vector:
	@staticmethod
	def  get1():
		vector . n = int(input('How  many  elements ?  :  '))   #  Adds  static  variable  'n'  to  class  vector  with  user  input
	def  get2(self):
		self . a  =  []  # Adds  variable  'a'  to  object  self  with  an  empty list
		for  i  in  range(vector . n):
			inp = int(input('Enter  any  number  :  '))
			self . a . append(inp) #  Appends  input  to  list  self . a
	def  add(self , x , y): #  self  is  object  'z'
		self . a =  []  # Adds  variable  'a'  to  object  'z'  with  an  empty list
		for  i  in   range(vector . n):
				self . a . append(x . a[i] + y . a[i])  #  Appends  the  result  to  the  list  z . a
vector . get1() #   Executes  static  method  of  vector  class
x = vector() #  3  empty  vector class  objects
y = vector()
z = vector()
print('1st  object')
x . get2()  #  Reads  inputs  into  the  list  'a'  held  by  object  'x'
print('2nd  object')
y . get2()  #  Reads  inputs  into  the  list  'a'  held  by  object  'y'
z . add(x , y)  #  Adds  the  lists  held  by  objects  'a'  and  'b'  and  stores  the  results  in  list  hely  by  object  'z'
print('Result :  '  ,  z . a)  #  prints  the  list  z . a


'''
static  variable  --->  n = 4

Object  'x'   --->  a =  [10 , 20 , 15 , 18]

Object  'y'   --->  a = [30 , 40 , 35 , 12]

Object  'z'   --->  a = [40 , 60 , 50 , 30]
'''
