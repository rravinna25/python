# Find  output (Home  work)
add = lambda  x , y : x + y #  Ref  add  points  to  lambda  function
print(type(add)) # <class  'function'>
print(add(10 , 20)) #  Executes  lambda  function  with  x  = 10 ,  y  = 20  and  result  is  30
print(add(10.6 , 20.8)) #  Executes  lambda  function  with  x  = 10.6 ,  y  = 20.8  and  result  is  31.4
print(add('Hyder' , 'abad'))  #  Executes  lambda  function  with  x  =  'Hyder' ,  y  =  'abad'  and  result  is  'Hyderabad'
print(add(True , False))   #  Executes  lambda  function  with  x  = True ,  y  =  False  and  result  is  1
print(add(25 , 10.8))   #  Executes  lambda  function  with  x  = 25 ,  y  = 10.8 and  result  is  35.8
print(add(3 + 4j , 5 + 6j))  #   #  Executes  lambda  function  with  x  =  3 + 4j ,  y =  5 + 6j  and  result  is  8 + 10j
#print(add(10 , '20')) #  Error  :   'x'  is  10 ,  'y'  is  '20'  and  10 + '20'  raises  error
#print(add()) # Error :  Lambda  function  expects  2  arguments  but  nothing  is  passed
print(add) #  type and address of lamda function



'''
add = lambda  a , b : a + b
How  to  define  regular  function  instead  of  lambda  function  ?  --->  def  add(a , b):
																													    return   a + b
'''
