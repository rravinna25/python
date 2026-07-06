# Save  in  any  file  of  cwd
import  p1 . mod1 , p1 . mod2   #  Imports  modules  mod1  and  mod2  of  package  p1  which  is  in  cwd
print(p1 . mod1 . x)  #  10 : Object  'x'  of   p1 . mod1  module  i.e.  10
p1 . mod1 . f1()  # Executes  function  f1()  of  p1 . mod1  module
a = p1 . mod1 . c1()   #  Creates  p1 . mod1 . c1  class  object
a . m1()  #  Execuets  method  m1()  of   p1 . mod1 . c1  class
print()
print()
print(p1 . mod2 . x)  #  20 : Object  'x'  of   p1 . mod2   module  
p1 . mod2 . f1()   # Executes  function  f1()  of  p1 . mod2  module
a = p1 . mod2 . c1()   #  Creates  p1 . mod2 . c1  class  object
a . m1()  #  Execuets  method  m1()  of   p1 . mod2 . c1  class


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1


1) import  p1
   What  does  the  statement  do ?  ---> Imports  package  p1  but  not  modules  of  the  package  p1

2) import  p1
    Is  p1 . mod1 . x  valid ?  ---> No  becoz  mod1  is  not  imported  from  package  p1  and  hence  mod1  can  not  be  used

3) import  mod1 , mod2
    Where  are  mod1  and  mod2  searched ?  --->  In  cwd
    What  is  the  issue ? ---> cwd  does  not  have  mod1  and   mod2  and  hence  raises  ModuleNotFoundError

4) import  p1 . mod1
    import  p1 . mod2
    How  to  reduce  the  two  statements  to  a  single  statement ?  ---> import  p1 . mod1 , p1 . mod2

5) import  p1 . mod1 , p1 . mod2
    Where  are  mod1  and  mod2  searched ?  ---> In  sub-directory  p1  but  not  in  cwd
	
6) import  p1 . mod1 , mod2	
    Where  are  mod1  and  mod2  searched ?  ---> Searches  for  mod1  in  sub-directory  p1   and  mod2  in  cwd
'''
