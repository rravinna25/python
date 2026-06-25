# copy()  method  demo  program  (Home  work)
a = {10 , 20 , 15 , 18}
print(a) # {10 , 20 , 15 , 18} in any order
b = a . copy()  # Copies  elements  of  set  'a' to  set  'b'
print(b) # {10 , 20 , 15 , 18} in any order
print(a  is  b) # False :  References  'a'  and  'b'  point  to different  sets
print(a  ==  b) # True :  Sets   a  and  b  have  same  elements
c  = a  # 'c' points  to  set  'a'
print(a  is  c) # True  :  References  'a'   and 'c'  point  to same  set


'''
1) What  does  copy()  method  do ?  --->  Returns  a  new  set  with  same  element

2) a = b
    What  does  the  statement  do ?  --->  Reference  copy
														 	      i.e.  id  is  copied

3) What  is  shallow  clone ?  ---> Reference  copy
     What  is  deep  clone ?  ---> Object  copy
'''
