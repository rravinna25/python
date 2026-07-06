# Save  in  any  file  of  cwd
import  p1 . __init__   #   Imports  p1 . __init__  module  and  automatically  executes  p1 . __init__  module
print(p1 . x)  # 10 : Object   'x'  of  p1 .  __init__  module 
p1 . f1()  #  Executes  function  f1()  of   p1 . __init__  module
a = p1 . c1()  #  Creates  p1 . __init__ . c1  class  object
a . m1()  #   Executes  method  m1()  of  p1 . __init__ . c1  class
print(p1 . __init__ . x)   #  10 : Object   'x'  of  p1 .  __init__  module  
p1 . __init__ . f1()   #  Executes  function  f1()  of   p1 . __init__  module
a = p1 . __init__ . c1()   #  Creates  p1 . __init__ . c1  class  object
a . m1()   #   Executes  method  m1()  of  p1 . __init__ . c1  class
#print(p1 . mod1 . x)  #  Error :  p1 . mod1  is  not  imported

'''
__init__   module  is  executed
__name__  :   p1
__init__   module  is  executed
__name__  :   p1.__init__
10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method
10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method


import  p1 . __init__
How  many  is  __init__  module  executed ?  --->  Twice  due  to  import  and  automatic  execution
'''
