# Save  in  any  file  of  cwd
from  p1  import  mod1  #  Imports  mod1   from  package  p1
print(mod1 . x) #  10 : Object  'x'  of   mod1   which  is  imported  from   package  p1  
mod1 . f1() #  Executes  function  f1()  of  mod1  which  is   imported  from   package  p1
a = mod1 . c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1()  #   Executes  method  m1()  of  class  c1  in  mod1  imported  from   package  p1
#print(p1 . mod1 . x) # Error :  Cannot  use  package  name  p1  as   it  is  not  imported
print()
print()
from  p1 . p2  import  mod2  #  Imports  mod2   from   sub-package  p2  which  is  in  package  p1
print(mod2 . x)  #  20 : Object  'x'  of   mod2   which  is  imported  from   sub-package  p2  of package  p1
mod2 . f1() #  Executes  function  f1()  of  mod2   which  is   imported  from   sub-package  p2  of  package  p1
a = mod2 . c1()  #  Creates  p1 . p2 . mod2 . c1  class  object
a . m1()  # Executes  method  m1()  of  class  c1  in  mod2 which  is   imported  from   sub-package  p2  of  package  p1
#print(p1 . p2 . mod2 . x) # Error :  Cannot  use  package  name  p1  as   it  is  not  imported
#from  p1  import   p2 . mod2  #  Error  :  import  clause  of  from  statement  cannot  use  '.'  
#from  p2  import  mod2 #  Error :  cwd  does  not  have  package  p2 


'''
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method


20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''
