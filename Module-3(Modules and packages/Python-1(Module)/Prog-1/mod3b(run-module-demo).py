#  Find  outputs  (Home  work)
import  runpy
print('Begin')
runpy . run_module('mod1') #  Executes  mod1  which  is  in  same  folder
#print(mod1 . x) #   Error :  Can  not  use  mod1  as  it  is  not  imported
#mod1 . f1()  #   Error :   Can  not  use  mod1  as  it  is  not  imported
#a = mod1 . c1()  #   Error :   Can  not  use  mod1  as  it  is  not  imported
print('End')
#run_module('mod1')  #  Error :  Current  module  does  not  have  run_module()  function 
#runpy . run_module(mod1)  #   Error :  Argument  should  be  string  module  but  not  module


'''
Begin
Hyd
Sec
Cyb
End


1) runpy . run_module('mod1')
    Do  we  need  to  import  mod1 ?  ---> No  becoz  mod1  is  not  being  used (It  is  string  'mod1'  but  not  module  mod1)

2) runpy . run_module('mod1')
    Is  function  of  mod1  executed ?  ---> No  becoz  it  is  not  being  called 
     Is  method  of  class  c1  in  mod1  executed ?  ---> No  becoz  it  is  not  being  called 

3) runpy . run_module('mod1')
    What  are  executed ?  ---> All  the  statements  of  mod1  
'''
