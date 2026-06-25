# Find  outputs
a = 10
b = 7
x = lambda  a , b :  a + b ,  a - b , a * b , a / b  #   A  tuple of  4  elements
print(type(x)) #  <class  'tuple'>
print(x)  #  (Type  and  address  of  lambda  function , 3 , 70 , 1.42)
for  y  in   x:   #   'y'  is   each  element  of  tuple   'x'
	print(y)  #   Type  and  address  of  lambda  function   <next  line> 3   <next  line>   70   <next  line>   1.42
print(x[0](9 , 2))  #  Executes  lambda  function  with  a = 9 ,  b = 2   and  result  is  9 + 2 = 11
print(x[1])  #  2nd  element  of  tuple  i.e.  3
#print(x())  #  Error :  Cannot  tuple  as  it  is  not  a  function


'''
<class 'tuple'>
(Type  and  address  of  lambda  function , 3, 70, 1.42)
Type  and  address  of  lambda  function
3
70
1.42
11
3
'''

'''
1) x = lambda  a , b :  (a + b ,  a - b , a * b , a / b)
    Is  'x'  lambda  function  (or)  tuple ?  ---> Lambda  function
    What  does  it  return ?  ---> Tuple  of  four  elements

2) x = lambda  a , b :  a + b ,  a - b , a * b , a / b
    Is  'x'  lambda  function  (or)  tuple ?  ---> Tuple  of  four  elements
    What  is  the  first  element  of  tuple ?  --->lambda  a , b : a + b
    What  does  lambda  function  return ?  ---> Result  of  a + b
    What  about  a - b , a * b  and  a / b ?   ---> They  are  tuple  elements  but  not  expressions  of  lambda  function
'''
