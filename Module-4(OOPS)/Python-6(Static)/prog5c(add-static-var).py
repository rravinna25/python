# How  to  add  static  variable  to  the  class  at  different  locations  of  the  program ?
class   c1:
	a = 10 # Adds  static  variable  'a'   to  class  c1   with  value  10
	def    __init__(self):  #  self  is  object  'x'
		c1 . b = 20 # Adds  static  variable  'b'   to  class  c1   with  value  20
		self. c = 30 # Adds  instance  variable  'c'  to   object  'x'  with  value  30
		#cls . k = 25 #  Error :  cls  does  not  exist   in  the  constructor
	def   m1(self):  # self  is  object  'x'
		c1 . d = 40  # Adds  static  variable  'd'  to  class  c1   with  value  40
		self . e = 50 # Adds  instance  variable  'e'   to   object  'x'  with  value  50
	@classmethod
	def   m2(cls):
		c1 . f = 60  # Adds  static  variable  'f'   to  class  c1   with  value   60
		cls . g = 70 #  Adds  static  variable  'g'   to  class  c1   with  value   70
		#self . k = 25 #  Error :  self  does  not  exist   in  method  m2()
	@staticmethod
	def   m3():
		c1 . h = 80 # Adds  static  variable  'h'   to  class  c1   with  value   80
		#self . k = 25 #  Error :  self  does  not  exist   in  method  m3()
		#cls . k = 35 #  Error :  cls  does  not  exist   in  method  m3()
#End  of  the  class
print('Begin')
print(c1 . __dict__)  #  {'a' : 10 , Ev's}
print()
print()
x = c1()  #  Constructor  initializes  object  'x'  with  c = 30  and  adds  static  variable  'b'  to  class  c1  with   value  20
print('Constructor')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20 , Ev's}
print()
print()
x . m1() #  Method  m1()  initializes  object  'x'  with  e = 50  and  adds  static  variable  'd'  to  class  c1  with   value  40
print('Instance  method  m1')
print(c1 .__dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40 , Ev's}
print()
print()
c1 . m2() #  class  method  m2()  adds  static  variables  'f'   and  'g'   to  class  c1  with  values  60  and  70  respectively
print('class  method   m2')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , Ev's}
print()
print()
c1 . m3() #  static  method  m3()  adds  static  variable  'h'  to  class  c1  with  value  80
print('static   method   m3')
print(c1 . __dict__)  #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80  , Ev's}
print()
print()
c1 . i = 90  # Adds  static  variable  'i'   to  class  c1   with  value   90
x . j = 100  #  Adds   instance  variable  'j'   to   object  'x'  with  value  100
print('Outside  the  class')
print(c1 . __dict__)   #  {'a' : 10 , 'b' : 20 , 'd' : 40 , 'f' : 60 , 'g' : 70 , 'h' : 80 , 'i' : 90 , Ev's}
print()
print()
print("Object  'x' ")
print(x . __dict__)  #  {'c' : 30 , 'e' :50 , 'j' : 100}


'''
static  variable  --->  a =  10 ,  b =  20 ,  d =  40 , f =  60 ,  g =  70 ,  h =  80 , i = 90

Object 'x'  --->  c =  30 ,  e = 50 ,  j =  100
'''
