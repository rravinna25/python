#  Find  outputs (Home  work)
large = lambda  x , y :  max(x , y) #  Ref  large  points  to  lambda  function
print(large(10 , 20))  #  20 : Executes  lambda  function  with  x  = 10 ,  y  = 20  
print(large(10.7 , 5.6))  #  10.7 : Executes  lambda  function  with  x  = 10.7 ,  y = 5.6 
print(large('g' , 's')) #  s : Executes  lambda  function  with  x =  'g' ,  y  = 's' 
print(large('Rama' , 'Rajesh')) #   Rama  : Executes  lambda  function  with  x = 'Rama'  , y = 'Rajesh'
print(large(True , False)) #  Executes  lambda  function  with  x = True ,  y  = False  and  result  is   True



'''
1) large  =  lambda   a  ,  b :   max(a , b)
    How  to  define  the  lambda  function  without  using  max()  function ?  --->
																							large = lambda  a , b :  a   if  a > b  else  b

2) large  =  lambda   x  ,  y :   if  x > y:  return  x  else:    return   y
    Is  the  statement  valid ? --->  No  becoz   lambda   function  can  not  use  if  and  return

3) In  other  words,   lambda  function  can  not  use  if , match ,  for  and  while

4) Can  lambda  function  use  ternary  operator  ?  --->  Yes
'''
