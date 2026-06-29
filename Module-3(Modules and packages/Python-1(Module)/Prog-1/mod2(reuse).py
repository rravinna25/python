# How  to  reuse  mod1  ?  (Home  work)
print('Begin')
import  mod1  #  imports  mod1  and  the  statements  of  mod1
print(mod1 . x)  #  Object  'x'  of  mod1  i.e. 25
mod1 . f1()  #  Executes  function  f1()  of  mod1
a = mod1 . c1()  #  Creates  mod1 . c1  class  object
a . m1()  #  Executes  method  of   class  mod1 . c1 
print('End')
#import  mod4    #  ModuleNotFoundError :  current  working  directory  does  not  have  mod4 
#print(x)  #  Error :  Current  module  does  not  have  object  'x'
#f1()  #  Error :  Current  module  does  not  have  function  f1()
#a = c1()  #  Error :  Current  module  does  not  have  class  c1


'''
Begin
Hyd
Sec
Cyb
25
Function
Method
End


1) How  many  statements  are  imported  from  mod1 ?  --->  Four

2) Where  does  mod1  resides ?  --->  In  current  working  directory  i.e.  Same  folder
'''
