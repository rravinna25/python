# Find  outputs  (Home  work)
class   c1:
	x = 10  #  Adds  static  variable  'x'  to  class  c1  with  value  10
	def  __init__(self):
		self . y = 20  # Adds  variable  'y'  to  object  self  with  value  20
	@classmethod
	def   m1(cls):
		cls . x = 30  #  Modifies  static variable  'x'  to 30
		cls . y = 40   #  Adds  static  variable  'y'  to  class  c1  with  value   40
# End  of  the  class
a = c1() #  Constructor  initializes  object  with  y = 20
b = c1() #  Constructor  initializes  object  with  y = 20
c1 . m1()  #  Executes  class  method  of  class  c1
print(a . x) # 30 :  static  variable  is  used  becoz  there  is  no  variable  'x'  in  object  'a'  
print(a . y) #  20 : Variable  'y'  of  object  'a' 
print(b . x) #  30 :  static  variable  is  used  becoz  there  is  no  variable  'x'  in  object  'a'  
print(b . y)  # 20 : Variable  'y'  of  object  'b'  
print(c1 . x , c1 . y) #   30 <space> 40  :  static  variables  of  class  c1  
#print(cls . x , cls . y) #  Error :  No  cls  outside  the  class
#print(self . x , self . y)   #  Error :  No  self  outside  the  class


'''
Static   variable   --->   x = 30 , y = 40

Object  'a'   --->  y = 20

Object  'b'   --->  y = 20


1) print(object . variable)
    Which  variable  is  used  ? ---> Instance  variable

2) print(classname . variable)
    Which  variable  is  used ? ---> Static  variable

3) print(cls . variable)
    Which  variable  is  used  ?  ---> Static  variable

4) Can  self  and  cls  be  used  outside  the  class  ?  ---> No

5) Who  can  use  cls ?  ---> Only  class  method

6) Who  can  use  self ?  --->  Instnace  method , constructor  and  destructor
'''
