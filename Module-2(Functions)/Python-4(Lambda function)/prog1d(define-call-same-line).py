# Find  outputs
print((lambda   x  :   x * x) (7)) #  Executes  lambda  function  with  'x'  =  7  and  result  is  49
print(lambda   x  :  x * x(7))  #  Type  and  address  of  lambda  function
print(lambda   x  :   x * x)   #  Type  and  address  of  lambda  function
print( (lambda  x = 25 :  x * x) () )  #  Executes  lambda  function  with  'x' =  default  value  25  and  result  is   625
square = lambda  x :  x  *  x  #  Ref  square  points  to   lambda  function
print(square(5)) #  Executes  lambda  function  with  'x'  =  5  and  result   is   25



'''
1) print((lambda  x :  x * x)(5))
    How  to  divide  the  statement  into  two  statements ?  ---> square = lambda  x  :  x * x  (This  is  Lambda  function  definition_
																							        print(square(5))  --->   lambda  function  call

2) What  does  print(lambda-function)  do ?  ---> Prints  type  and  address  of  lambda  function

3) When  is  lambda  function  lost ?  --->  When  it  does  not  have  any  reference
    When  is  lambda  function  alive ?  --->  As  long  as  it  has  a  reference

4) print( lambda   x  :  x * x(7))
    What  are  multiplied ?  ---> x  and  result  of  x(7)
'''
