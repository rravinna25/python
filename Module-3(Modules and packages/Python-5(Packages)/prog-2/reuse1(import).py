#  Save  in  any  file  of  cwd
import  p1 . mod1 , p1 . p2 . mod2  #  Import  mod1  from  package  p1  and  mod2  from  sub-package  p2  of  package  p1
print(p1 . mod1 . x) #  10 : Object  'x'  of   p1 . mod1  module  
p1 . mod1 . f1()   # Executes  function  f1()  of  p1 . mod1  module
a = p1 . mod1 . c1()  #  Creates  p1 . mod1 . c1  class  object
a . m1()   #  Execuets  method  m1()  of   p1 . mod1 . c1  class
print()
print()
print(p1 . p2 . mod2 . x) # 20 : Object  'x'  of   p1 . p2 . mod2  module  
p1 . p2 . mod2 . f1()  # Executes  function  f1()  of  p1 . p2 . mod2  module
a = p1 . p2 . mod2 . c1()  #  Creates  p1 . p2 . mod2 . c1  class  object
a . m1()   #  Execuets  method  m1()  of   p1 . p2 . mod2 . c1  class


'''
10
p1  --->  mod1  --->  f1 function
p1 ---> mod1 ---> c1 ---> m1 method
20
p1 ---> p2 ---> mod2 ---> f1 function
p1 ---> p2 ---> mod2 ---> c1 ---> m1 method
'''
