# Save  in  any  file  of  cwd
from  p1 . mod1   import  * #   Imports  all  the  members  of  p1 . mod1  and  automatically  executes  p1 . __init__  module
print(x) #  20 : Object  'x'  of p1 .  mod1
f1() # Executes  function  f1()  of  p1 . mod1
a = c1()  #  Creates  p1 . mod1 . c1  class object
a . m1()  #  Executes  method  m1()  of  p1 . mod1 . c1  class
#print(p1 . x)  #  Error :  Cannot  use  package  name  p1  as  it  is  not  imported  nor  any  module  of  p1  is  imported  (with  import  statement)
#print(p1 . __init__ . x)   #  Error :  Cannot  use  package  name  p1  as  p1  is  not  imported  nor  any  module  of  p1  is  imported  (with  import  statement)
#print(__init__ . x)   #  Error :  __init__  module  is  not  imported
#from  p1  import  mod1 . * #  Error :  import  clause  of  from  statement  can  not  use  '.'  


'''
__init__   module  is  executed
__name__  :   p1
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method



1) from  p1  . mod1  import  *
    Can  members  of  p1 . mod1  be  used ?  ---> Yes  becoz  they  are  imported
    Can  members  of  __init__  module  be  used ?  --->   No  becoz  __init__  module  is  not  imported  from   package  p1
                                                                                        even  though   __init__  module  is   executed
2) import  p1
    import  p1 . mod1
    from  p1  import  mod1
    from  p1 . mod1  import  *
    Which  statement  permits  us  to  use  members  of  __init__ module ?  ---> Only  first  two  statements
'''
