# Save  in  any  file  of  cwd
from  p1 . mod1  import  *  #  Imports  all  the  members  of  mod1  which  is  in  package  p1
print(x) #  10 : Object  'x'  which  is  imported  from  p1 . mod1  
f1() #  Executes  function  f1()  which  is  imported  from  p1 . mod1
a = c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1()  #  Executes  method  m1()  of  class  c1  which  is   imported  from  p1 . mod1
print()
print()
from  p1 . p2 . mod2  import  *   #  Import  all  the  members  of  mod2  which  is  in  sub-package  p2  of   package  p1
print(x)  #  20 : Object  'x'  which  is  imported  from  p1 . p2 . mod2  
f1() #  Executes  function  f1()  which  is  imported  from  p1 . p2 . mod2
a = c1()  #  Creates  p1 . p2 . mod2 . c1  class  object
a . m1()  #  Executes  method  m1()  of  class  c1  which  is   imported  from  p1 . p2 . mod2
#from  p1  import  mod1 . *  #  Error : import  clause  of  from  statement  can  not  use  '.'  


'''
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''
