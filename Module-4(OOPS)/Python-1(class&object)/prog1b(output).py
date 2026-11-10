# Find  outputs  (Home  work)
class   c1:  #  Empty  class
	pass
# End  of  the  class
a = c1()    #   Creates  an  empty  c1 class object
print(id(a)) #  Address of   object  'a'
print(type(a)) #  <class  '__main__ . c1'>  i.e. Type  of  object  'a'  
print(a . __dict__) #  {}  i.e. Converts  empty  object   'a'  to  {}
print(a) #   __str__()  method  of  object  class   returns  type  and  address  of  object  'a'
del  a #  Deletes  object  'a'
#print(a) #  Error :  Object  'a'  does   not  exist




'''
1) a =  c1()
    print(a)
	Which  method  is  executed ?  ---> __str__()  method 
	Which  class  __str__()  method  is  executed  and  why ?  ---> __str__()  method  of  object  becoz  class  c1  does  not 
																									   have  __str__()  method

2) What  is  object  class ?  ---> Parent  class  to  all  python  classes

3) Where   is  object  class  defined ?  ---> In  builtins  module

4) What  does  __str__()  method  of  object  class  do ?   ---> Returns  type  and  address  of  the  object
																									Eg: class   object:
																												   def   __str__(self):
																															returns  type  and  address  of  object
																															
5) Which  function  returns  decimal  address ?  --->  id()  function 
     Which  method  returns  hexa-decimal  address ?  ---> __str__()  method  of  object  class
'''
