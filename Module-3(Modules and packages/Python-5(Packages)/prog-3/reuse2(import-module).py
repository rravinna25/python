# Save  in  any  file  of  cwd
import  p1 . mod1 #   Imports  p1 . mod1  and  automatically  executes  p1 . __init__  module  
print(p1 . mod1 . x) #  20 : Object  'x'  of  p1 . mod1   
p1 . mod1 . f1() #  Executes  function  f1()  of  p1 . mod1
a = p1 . mod1 . c1()   #  Creates  p1 . mod . c1  class  object
a . m1()  #  Executes  method  m1()  of  p1 . mod1 . c1  class
print()
print()
print(p1 . x) #  10 : Object  'x'  of  p1 . __init__  module  
p1 . f1() #   Executes  function  f1()  of  p1 . __init__  module
a = p1 . c1() # Creates  p1 . __init__ . c1  class  object
a . m1()  #  Executes  method  m1()  of  p1 . __init__ . c1  class
#print(p1 . __init__ . x)  #  Error :  p1 . __init__  module  is  not  imported
#p1 . __init__ . f1()  #   Error :  p1 . __init__  module  is  not  imported
#a = p1 . __init__ . c1()   #   Error :  p1 . __init__  module  is  not  imported



'''
__init__   module  is  executed
__name__  :   p1
20
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method


10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method
'''
