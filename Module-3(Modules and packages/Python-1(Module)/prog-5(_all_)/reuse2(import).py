#  Find  outputs
import  calc  #  Imports  calc  module  and  statements  of  calc  module  i.e.  Ignorees  __all__  list  
print(calc . x)  #  Object  'x'  of  calc  module  i.e.  100
print(calc . y)   #  Object  'y'  of  calc  module  i.e.  200
print(calc . add(10 , 7))  #  Executes  add()  function  of  calc  module  i.e.  17
print(calc . sub(10 , 7))    #  Executes  sub()  function  of  calc  module  i.e.  3
print(calc . mul(10 , 7))   #  Executes   mul()  function  of  calc  module  i.e.  70
print(calc . div(10 , 7))    #  Executes  div()  function  of  calc  module  i.e.  1.42
a = calc . c1() # creates  calc . c1  class object
a . m1()   #  Executes  method  of  calc . c1  class


'''
100
200
17
3
70
1.42
m1 method



1) import calc
    We  can  use  all  the  members  of  cal  module  becoz  cal  module  is  imported

2) It  doesn't  matter  what  __all__  list  contains  becoz  module  is  imported  but  not  members
'''
