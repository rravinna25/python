#  intersection()   method  demo  program (Home  work)
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . intersection(b)  #  Returns  a  new  set  with  common  elements  of  sets  'a'  and  'b'
print(c) # {30 , 40}  in  any  order
print(type(c)) # <class 'set'>
d = a & b   #  A  set  with  common  elements  of  sets  'a'  and  'b'
print(d) # {30 , 40}  in  any  order
print(type(d)) # <class 'set'>
print(c  is  d) # False :  References  'c'  and  'd'  point  to  different  sets
print(c  ==  d) # True  :  Sets  'c'  and  'd'  have  same  elements


'''
intersection()  method
---------------------------
1) What  does  a . intersection(b)  do ?  --->  Returns  a  set  with  common  elements  of  sets   'a'  and  'b'

2) set . intersection(list) 
    Is  the  statement  valid ?  ---> Yes  becoz  argument  of  intersection()  method  can  be  any  sequence  but  not  necessarily  set

3) What  is  another  way  to  obtain  common  elements ?  --->  a & b

4) Is  set & list  valid ?  --->  No  becoz  operands  of  &  operator  should  be  sets  only

5) list . intersection(set) 
     Is  the  statement  valid ?  --->  No  becoz  list  does  not  set  have  intersection()  method
'''
