#  Save  in  any  file  of  cwd
from  p1 . mod1  import  *  #  Imports  all  the  members  of  p1 . mod1  module
print(x) #  10 : Object  'x'  imported  from  p1 . mod1  module 
f1() #  Executes  function  f1()  imported  from  p1 . mod1  module
a = c1() #   Creates  p1 . mod1 . c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  imported  from  p1 . mod1  module
print()
print()
from  p1 . mod2  import  *   #  Imports  all  the  members  of  p1 . mod2  module
print(x) # 20 : Object  'x'  imported  from  p1 . mod2  module 
f1() #  Executes  function  f1()  imported  from  p1 . mod2  module
a = c1()  #  Creates  p1 . mod2 . c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  imported  from  p1 . mod2  module
#print(p1 . mod1 . x) #  Error :  Can  not  use  package  p1  as  it  is not imported
#print(mod1 . x) #  Error :   Can  not  use  module  mod1   as  it  is not imported
#from  p1   import  mod1 . *   #  Error  :  import  clause  of  from  statement  cannot  have  '.'  


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''


'''
1) from   p1  import  mod1
    from   p1  import  mod2
    How  to  combine  the  two  statements  to  a  single  statement ?  ---> from  p1  import  mod1 , mod2

2) from  p1 . mod1 , p1 . mod2  import  *
    Is  the  statement  valid ?  --->  
												No  becoz  from  statement  can  import  members  of  single  module  but  not  
												memebrs  of  multiple  modules

3) import  p1 . mod1 , p1 . mod2
    Is  the  statement  valid ?  ---> Yes  becoz  import  statement  can  inport  multiple  modules

4) import  p1 . mod1 , mod2
    What  are  imported ?  ---> mod1  from  package  p1  and  mod2  from  cwd
'''
