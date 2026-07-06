# Save  in  any  file  of  cwd
import   p1   #   imports  package  p1  and   automatically  executes  __init__  module of package  p1
print(p1 . x)  #  10 : Object  'x'  of  p1 . __init__  module  
p1 . f1()  #   Executes  function  f1()  of  p1 . __init__  module
a = p1 . c1()  #  Creates  p1 . __init__ . c1   class  object
a . m1() #  Executes  method  m1()  of  p1 . mod1 . c1  class
#print(p1 . __init__ . x)   #  Error  :  p1 . __init__  is   not  imported
#print(__init__ . x)   #  Error :  cwd  does  not  have  __init__  module  
#print(x)  #  Error :   Current  module  does  not  have  object   'x'
#print(p1 . mod1 . x)   #   Error :  p1 . mod1  is  not  imported


'''
__init__   module  is  executed
__name__  :   p1
10
package  p1 ---> __init__  module ---> f1  function
package  p1 ---> __init__  module ---> class  c1  ---> m1  method
'''
