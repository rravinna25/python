# Find  outputs  (Home  work)
class   c1:
	def   __init__(self):
		self . x = 10
		self . y = 20
		self . z = 30
#end  of  the  class
a = c1() #  Constuctor  initializes  object  with  x = 10 , y = 20 , z = 30
b = c1() #  Constuctor  initializes  object  with  x = 10 , y = 20 , z = 30
print(a . __dict__) # {'x' : 10 , 'y' : 20 , 'z' : 30}
print(b . __dict__) # {'x' : 10 , 'y' : 20 , 'z' : 30}
del  a . x  #  Removes  variable  'x'  from  object  'a'
del  b . y  #  Removes  variable  'y'  from  object  'b'
print(a . __dict__) # {'y' : 20 , 'z' : 30}
print(b . __dict__)  # {'x' : 10 , 'z' : 30}
#print(a . x) # Error :  Object  'a'  does  not  have  variable  'x' 
#print(b . y) # Error :  Object  'b'  does  not  have  variable  'y'


'''
Object  'a'   --->  y = 20 , z = 30  

Object  'b'   ---> x = 10 , z = 30


1) What  does  del  a . x  do ?  --->  Removes  variable  'x'  of  object   'a'

2) What  does  del   a   do ?   --->  Deletes  object  'a'

3) The  above  program  demonstrates  that  python  object  is  shrinkable
'''
