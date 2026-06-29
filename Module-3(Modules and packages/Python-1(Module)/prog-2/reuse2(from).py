# How  to  use  members  of  cal  module  with  from  statement ?  (Home  work)
print('Begin') # Begin
from  cal  import  *  #  Imports  all  the  members  and  statements  of  cal  module
print(x) #  100 :  Object  'x'   imported  from   cal   module  
print(y)  # 200 : Object  'y'   imported  from   cal   module  
#print(cal . x) #  Error :  Cannot  use  cal  module  as  it  is  not  imported
print(add(10 , 7)) #  17 : Executes  add()  function  imported   from  cal  module  
print(sub(10 , 7))  #  3 : Executes  sub()  function  imported   from  cal  module 
print(mul(10 , 7)) #  70 : Executes  mul()  function  imported   from  cal  module  
print(div(10 , 7)) #  1.42  :  Executes  div()  function  imported   from  cal  module 
#print(cal . add(x , y)) #  Error :  Cannot  use  cal  module  as  it  is  not  imported
a = c1() #  Creates  mod1 . c1  class  object
a . m1()  #  Executes  method  m1  of  mod1 . c1  class  as   'a'  is  mod1 . c1  class  object
#b = cal . c1()  #  Error :  Cannot  use  cal  module  as  it  is  not  imported


'''
Begin
100
200
17
3
70
1.42
m1  method
'''
