# Save  in  any  file  of  cwd
from  p1   import  mod1  # Imports  mod1  from  package  p1  and  automatically  executes  p1 . __init__  module
print(mod1 . x)  #  20 : Object  'x'  of  mod1  imported  package  p1  
mod1 . f1()  #  Executes  function  f1()  of  mod1  imported  package  p1
a = mod1 . c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  in  mod1   imported  package  p1
#print(p1 . x)  #  Error :  Cannot  use  package  name  p1  as  it  is  not  imported  nor  any  module  of  p1  is  imported  (with  import  statement)
#print(p1 . __init__ . x)   #  Error :  Cannot  use  package  name  p1  as  p1  is  not  imported  nor  any  module  of  p1  is  imported  (with  import  statement)
#print(__init__ . x)   #  Error :  __init__  module  is  not  imported


'''
__init__   module  is  executed
__name__  :   p1
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method



from  p1  import  mod1
Can  members  of  mod1  be  used ?  --->  Yes  with  mod1 . member
Can  members  of  __init__  module  be  used ?  ---> No  becoz  __init__  is  not  imported  
'''
