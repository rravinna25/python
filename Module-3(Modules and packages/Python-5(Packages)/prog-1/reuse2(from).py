#  Save  in  any  file  of  cwd  (Homework)  --->   Don'r  run
from  p1  import  mod1 , mod2  #   Imports  modules   mod1   and  mod2  from  package  p1  which  is  in  cwd
print(mod1 . x) # 10 : Object  'x'  of  mod1  imported  from  package  p1 
mod1 . f1() #   Executes  function  f1()  of  mod1  imported  from  package  p1
a = mod1 . c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  in  mod1  imported  from   package  p1
print()
print()
print(mod2 . x) #  20 : Object  'x'  of  mod2  imported  from  package  p1
mod2 . f1()  #  Executes  function  f1()  of  mod2  imported  from  package  p1
a = mod2 . c1() # Creates  p1 . mod2 . c1  class  object
a . m1()  #  Executes  method  m1()  of  class  c1  in  mod2  imported  from   package  p1
#print(p1 . mod1 . x)  # Error :  Cannot  use  package  p1   as  it  is not imported
#print(x) #  Error :   Current module  does  not  have   object  'x'


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''
