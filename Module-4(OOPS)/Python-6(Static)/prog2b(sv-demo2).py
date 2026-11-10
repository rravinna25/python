# Find  outputs (Home  work)
class c1:
    x = 10  #  Adds  static  variable  'x'  to  class  c1  with  value  10
    def __init__(self):
	    self . y = 20   # Adds  variable  'y'  to  object  self  with  value  20
a = c1() #  Constructor  initializes  object  with  y = 20
b = c1()   #  Constructor  initializes  object  with  y = 20
a . x += 1 #  a . x = a . x + 1  --->  a . x  = 10 + 1 = 11  i.e.  Adds  variable  'x'  to  object  'a'  with  value  11
b . y += 1 #  Increments  b . y  by   1
print(a . x) #  11 :  Variable  'x'  of  object  'a'  
print(a . y) #  20 : Variable  'y'  of  object  'a' 
print(b . x) #  10 : static  variable  is  used  as  there  is  no  variable  'x'  in   object  'b' 
print(b . y)  #  21 :  Variable  'y'  of  object  'b'  
print(c1 . x) #  10 : static  variable  'x'  of  class  c1   
print(a . __dict__) # {'y' : 20 , 'x' : 11}
print(b . __dict__) # {'y' : 21}
print(c1 . __dict__) # {'x' : 10 , Ev's}


'''
static   variable  --->   x = 10

Object  'a'  --->  y = 20 ,  x  =  11

Object  'b'  --->  y = 21


1) What  is  the  expansion  for  a . x += 1  ? --->  a . x = a . x + 1

2) Which  variable  is  accessed  for  a . x  on  right  side ?  --->  Static  variable  becoz  object  'a'  does  not  have  variable  'x'

3) What  does  a . x  on  left  side  do ?  --->  Adds  variable  'x'  to  object   'a'  becoz  object  'a'  does  not  have  variable  'x'  
'''
