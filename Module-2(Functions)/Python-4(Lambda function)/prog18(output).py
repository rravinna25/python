# Find  output  (Home  work)
add = lambda  x  :   x == 25   #  Ref  add  points  to  lambda  function
print(add(10)) #   False : Executes  lambda  function  with  x = 10  which  returns  10 == 25  
add = lambda  x = 25 :   x == 35  #  Ref  add  points  to  another  lambda  function
print(add())  #  False : Executes  lambda  function  with  x =  default  value  25  which  returns  25 == 35 
#add = lambda  x  :   x = 25  #  Error :  Lambda  function  can  not  modify  argument 'x'
#add = lambda  x  :   x := 25  #  Error :  Lambda  function  can  not  modify  argument  'x'



'''
1) Can  regular  function  modify  value  of  argument  ?  --->  Yes

2) What  about  lambda   function  ?  --->  No  and  the  argument  is  treated  as   read  only  argument  in  lambda  function
'''
