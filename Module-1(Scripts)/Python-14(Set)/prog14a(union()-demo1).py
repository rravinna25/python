# union()  method  demo  program
a = {10 , 20 , 30 , 40}
b = {30 , 40 , 50 , 60}
c = a . union(b) #  Concatenates  sets  'a'  and  'b'  to  form a  new  set
print(c) #  {10 , 20 , 30 , 40 , 50 , 60}  in  any  order
print(type(c)) #  <class  'set'>
d = a | b  #  Concatenates  sets  'a'  and  'b'  to  form a  new  set
print(d) #  {10 , 20 , 30 , 40 , 50 , 60}  in  any  order
print(type(d)) #  <class  'set'>
print(c  is  d)  #  False  :  References  'c'  and  'd'  point  to  different  sets  as  set  is  not  reusable
print(c  ==  d)  # True :  Sets   'c'  and  'd'  have  same  elements
#print(a + b)  #  Error :  Sets  can  not  be concatenated  with  +  operator


'''
union()  method
------------------
1) What  does  a . union(b)  do ?  --->  Concatenates  sets  'a'  and  'b'  to  form  a  new  set  
																		and  
														    returns  the  new  set

2) a . union(b)
    Is  set  'a'   modified  after  execution  of  union()  method  ?  --->  No  becoz  results  are  stored  in  a  new  set

3) set . union(list)  
    Can  set  and  list  be  concatenated  with  union()  method ?  --->  
												Yes  becoz  argument  of  union()  method  can  be  any  sequence  but  not  necessarily  set

4) What  is  another  way  to  concatenate  two  sets ?  --->  a | b

5) Is  set + set  valid ?  --->  No  becoz  sets  can  not  be  concatenated  with  +  operator

6) set | list  
    Can  set  and  list  be  concatenated  with  |  operator ?  --->  
																		No  becoz  operands  of  |  operator  should  be  either  sets  (or)  dictionaries

7) list . union(set)  
     Is  the  statement  valid ?  --->  No  becoz  list  does  not  have  union()  method  
'''
