# Find  outputs
a  =  lambda  :  print('Hyd')  ;  print('Sec');  print('Cyb')  #  1st   statement  is  in  lambda  function  and  rest  outside
print(a()) #  Executes  lambda  function  which  prints  'Hyd'  and  returns  None  i.e.  print(None)  prints  None

'''
Sec
Cyb
Hyd
None


1) What  does  print('Hyd')  do  ?   --->  Prints   'Hyd'  and   returns  None

2) a  =  lambda  :  print('Hyd'); 
   How  is  the  lambda  function  definition  reduced  to ?   --->  a = lambda  :  None

3) What  does  a()  do ?  --->  returns  None

4) print(a())
    How  is  the  statement  reduced  do ?   --->  print(None)
'''
