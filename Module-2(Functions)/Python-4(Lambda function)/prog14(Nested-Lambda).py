 # Nested  lambda  function  (Home  work)
add  =  lambda    x = 10   :    lambda   y  :  x  +  y  #   Ref  add  points  to  outer  lambda  function
a = add()  #  Executes  outer  lambda  function  with  x = default  value  10  which  returns   inner  lambda  function  i.e. a = lambda  y : 10 + y
print(a(20))  #  Executes   inner  lambda  function  with  y =  20  which  returns  10 + 20 = 30
print(add(30)(40)) # print((lambda  y :  30 + y)(40))  =  70


'''
1) Where  does  reference  add  points  to  ?  --->  outer  lambda  function

2) What  is  executed  for  add() ?  --->  outer  lambda  function  with  default  value  10

3) What  does  add()  return ?  --->  Inner  lambda  function
													     i.e.  lambda   y : 10 +  y

4) Where  does  reference  'a'  points  to  ?  ---> Inner  lambda  function

5) What  is  executed  for  a(20) ?  --->  inner  lambda  function  with  y = 20

6) How  many  lambda  functions  are  executed  for  add(30)(40) ?  --->  Two

7) What  does  add(30)  return ?  ---> Inner  lambda  function
															i.e.  lambda  y : 30 + y
'''
