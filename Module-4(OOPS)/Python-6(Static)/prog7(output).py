# Find  outputs  (Home  work)
class  c1:
        a , b , c  = range(1 , 4) #  Adds  3  static  variables  to  class  c1  with  values  1 , 2 , 3  respectively
# End  of  the  class
print(c1 . a) #  1 : static   variable   'a'  of  class   c1  
print(c1 . b)  #  2 : static   variable   'b'  of  class   c1  
print(c1 . c) #  3 : static   variable   'c'  of  class   c1  
print(c1 . __dict__)  #  {'a' : 1 , 'b' : 2 , 'c' : 3 , Ev's} :  All  the  static  variables  of  class  c1  and  Environment  variables




'''
1) a , b , c  =  range(1 , 5)
   Is  the  statement  valid ?  --->  No  becoz  range  object  has  got  excess  elements

2) a , b , c  =  range(1 , 3)
    Is  the  statement  valid ?  --->  No  becoz  range  object  has  got  few  elements
'''
