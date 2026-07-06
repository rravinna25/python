#  Save  in  any  file   of  cwd
import  p1 . mod1  #  Imports  p1 . mod1  and  automatically  executes  p1 . __init__   module  which  imports  p1 . mod1  and  p1 . mod2
p1 . mod1 . f1()   #   Executes  function  f1()  of   p1 . mod1
p1 . mod2 . f1()  #   Executes  function  f1()  of   p1 . mod2


'''
1) import  p1
    What  are  the  three  events ?  ---> a) imports  package  p1
														      b) Executes  __init__  module  of  package  p1
															  c) Imports  modules  mod1  and  mod2  of  package  p1
															      due  to  the  import  statements  in  p1 .  __init__  module

2) What  is  the  advantage  of  __init__  module ?   --->  It  is  used  to  import  all  the  modules  of  same  package
'''
