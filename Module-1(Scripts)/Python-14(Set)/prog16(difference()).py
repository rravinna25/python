# difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . difference(b)  #  Returns  a  set  with  those  elements  of   set  'a'  which  are  not  in  'b'
print(c) # {10 , 20}  in  any  order
print(type(c)) # <class 'set'>
d = a - b   #  A  set  with  those  elements  of   set  'a'  which  are  not  in  'b'
print(d) #  {10 , 20}  in  any  order
print(type(d)) # <class'set'>
print(c  is  d) # False  :  References  'c'  and  'd'  point to  different  sets
print(c  ==  d) # True  :  Sets  'c'  and  'd'  have same  elements


'''
difference()  method
------------------------
1) What  does  a . difference(b)  do ? --->  Returns  a  set  with  those  elements  of  set  'a'  which  are  not  in  'b'

2) set . difference(list) 
    Is  the  statement  valid ?  ---> Yes  becoz  argument  of  difference()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . difference(b) ?  --->  a - b

4) Is  set - list  valid ?  --->  No  becoz  operands  of  -  operator  should  be  sets  only
'''
