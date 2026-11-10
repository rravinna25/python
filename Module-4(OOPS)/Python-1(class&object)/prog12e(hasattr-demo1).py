#  Find  outputs  (Home  work)
class   rat:
	x = 25  #  'x'  is  static  variable  which  is  global  to  all  rat  class  objects
	def    m1():
		pass
# End  of  the  class
a = rat() #  Creates  an  empty  rat  class  object
a . nr = 22  # Adds  variable  nr  to  object  'a'  with   value  22
print(hasattr(a , 'nr')) #   True :  Object  'a'  has  variable  'nr'  
print(hasattr(a , 'dr'))  #   False :  Object  'a'  does  not  have  variable  'dr'  
print(hasattr(a , 'm1'))  #   True :   rat  class  has  method  'm1'
print(hasattr(a , 'm2'))  #  False :  rat  class  does  not  have  method  'm2'  
print(hasattr(rat , 'm1'))  #   True :  rat  class  has  method  'm1'
print(hasattr(rat , 'm2'))  #  False :  rat  class  does  not  have  method  'm2'  
print(hasattr(rat , 'nr'))   #  False :  rat  class  does  not  have  method  'nr'  
print(hasattr(rat , 'x'))   # True :  rat  class  does  static  variable  'x'
print(hasattr(a , 'x'))   # True :  Object  'a'  has  static  variable  'x'


'''
Object  'a'  --->  nr = 22

static  variable  --->  x = 25

Where  is  static  variable  initialized ?  --->  Inside  the  class
'''
