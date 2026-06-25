# Lambda  function  to  find  square  of  a  number
square = lambda  x  :  x * x
print(square(5))  #  'x'  is   5  and  result  is  25
print(square(2.5))  #  'x'  is   2.5  and  result  is  6.25
print(square(True))  #  'x'  is   True  and  result  is  1
print(square(3 + 4j))  #  'x'  is   3 + 4j  and  result  is   (3 + 4j) * (3 + 4j) = 9 + 12j + 12j - 16 = -7 + 24j
print(square(x = 10))  #  'x'  is   10  and  result  is  100
#print(square())  #  Error :  Arg  is  not  passed   for  'x'
print(square)  #  Type and  address  of  lambda  function
print(type(square))  #  <class  'function'>
print(id(square))  #  Address  of  lambda  function


'''
1) square =  lambda   x  :   x * x
    Where  does  reference  square  points  to ?  ---> Lambda   function

2) How  is  lambda  function  called ?  --->  Through  refernce  square
																    i.e.  square(5)

3) square = lambda  x :  x * x
    How  to  replace  the  lambda  function  with  regular  function ?  --->  def   square(x):
											                              											 	   return   x *  x
'''
