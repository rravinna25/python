#  Find  outputs  (Home  work)
s = 'Hyd'
print(lambda  s  :  print(s)) # Type and address of the lambda function
print(lambda  x  :  print(x) (s)) # Type and address of the lambda function
print((lambda  x  :  print(x)) (s)) # Executes  lambda  function  which  prints  'Hyd'  and  returns  None  and  print(None)   prints  None
(lambda  x  :  print(x)) (s)  # Executes  lambda  function  which  prints  'Hyd'  and  returns  None  and  None  gets  ignored


'''
1) print(lambda-function) 
   What  is  printed ?  --->  Type  and  address  of  lambda  function

2) (lambda  x  :  print(x)) (s)
    What  are  's'  and  'x'  called  ? ---> 's'  is  actual  parameter  and  x  is  formal  parameter

3) s = 'Hyd'
    print((lambda  x  :  print(x)) (s))
    What  does  lambda  function  do ?  ---> Prints  Hyd  and  returns  None 
    What  does  outer  print()  do ?  --->  Prints   None
'''
