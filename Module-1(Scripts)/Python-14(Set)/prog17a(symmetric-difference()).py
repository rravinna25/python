# symmetric_difference()   method  demo  program  (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . symmetric_difference(b)  #  Returns  a  set  with  all  the  elements  of  sets  'a'  and  'b'   without  common  elements
print(c) # {10 , 20 , 50 , 60}  in  any  order
print(type(c)) # <class 'set'>
d = a ^ b  #  A  set  with  all  the  elements  of  sets  'a'  and  'b'   without  common  elements
print(d) # {10 , 20 , 50 , 60}  in  any  order
print(type(d)) # <class 'set'>
print(c   is   d) # False :  References  'c'  and  'd'  point  to  different  sets
print(c  ==   d) # True :  Sets  'c'  and 'd'  have  same  elements



'''
symmetric_difference()  method
---------------------------------------
1) What  does  a . symmetric_difference(b)  do ? --->  Returns  a  set  with  all  the  elements  of  sets   'a'  and  'b'  but
						                                                              without  common  elements
																					  i.e.  Union  -  Intersection

2) Is  set . symmetric_difference(list)  valid  ?  --->  Yes  becoz  argument  can  be  any  sequence  but  not  necessarily  set

3) What  is  the  alternative  to  a . symmetric_difference(b) ?  --->  a ^ b

4) Is  set ^ list  valid ?  --->  No  becoz  operands  of  ^  operator  should  be  sets  only
'''
