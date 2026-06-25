#  Identify  Error
def   f1():
        nonlocal   x  #  Error :  f1()  is  not  inner  function  and  nonlocal  keyword  cannot  be  used


'''
1) What  are  the  two  pre-requisites  to  use  nonlocal  keyword ?  --->
																		a) Only  inner  function  can   use  nonlocal  keyword
																		b) Outer()  function  should  have  a  Lv  with  same  name

2) What  are  the  pre-requisites  to  use  global  keyword ?  ---> Nothing
																	i.e.  Any  function  can  use  global  keyword  even  though  there  is  no  Gv
'''
