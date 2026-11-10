# Find  outputs (Home  work)
class c1:
    x = 10  #   Adds  static  variable  'x'  to   class  c1  with  value  10
    def  __init__(self):
	    self . y = 20
a = c1()  #  Constructor  initializes   object  with  y  = 20 
b = c1()  #  Constructor  initializes   object  with  y  = 20 
a . x = 30 # Adds  variable  'x'  to  object  'a'  with  value  30
b . y = 40 # Modifies  b . y  to  40
print(b . x) #  10 :  Static  variable  'x'  becoz  object  'b'  does  not  have  variable  'x'
print(b . y) #  40 :  Variable  'y'  of  object  'b'  
print(a . x)  #  30 :  Variable  'x'  of  object  'a'  
print(a . y)  #  20 : Variable  'y'  of  object  'a' 
print(c1 . x) #  10 : static  variable  'x'  of  class  c1  
print(a . __dict__) #  {'y' : 20 , 'x' : 30}
print(b . __dict__)  # {'y' : 40}
print(c1 . __dict__) # {'x' : 10 , Ev's}


'''
static  variable   --->   x  = 10

Object  'a'  --->  y = 20 , x = 30

Object  'b'  --->  y = 40
'''
