# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()  #  Ref  'b'  points  to  a  new  list  of  same  elements  in  list  'a'
print(b)  # [10 , 20 , 15 , 18]
print(a  is  b) # False :  References  'a'  and  'b'  point  to  different  lists
print(a  ==  b) # True :  Lists  'a'  and  'b'  have  same  elements
c = a[:]  #   Ref  c  points  to  a  new  list  of  same  elements in  list   'a'
print(c) # [10 , 20 , 15 , 18]
print(a  is  c) # False :  References 'a'  and  'c'  point  to  different  lists
print(a  ==  c) # True :  Lists  'a'  and  'c'  have  same  elements
d = a # Reference  'd'  points  to  same  list  where 'a' points
print(d) # [10 , 20 , 15 , 18]
print(a  is  d) # True  :  References  'a'  and  'd'  point  to  same  list
print(a  ==  d) # True :  Lists  'a'  and  'd'  have  same  elements





'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Copies  elements of  list  to  a  new  list  and  returns  the  new  list

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  ---> b = a[:]
	
3) b = a
    b = a[:]
	What  is  the  difference  ?  --->  b = a  assigns  ref  'b'  to  list  'a'  but
	                                                     b = a[:]  assigns  ref  'b'  to  a  new  list  which  has  all  the  elements  of  list  'a'
'''
