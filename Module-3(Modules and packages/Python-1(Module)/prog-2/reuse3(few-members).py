# How  to  import  only  variable  'x' ,  functions  add()   and  mul()  and  class  c1  of  cal  module ?  (Home  work)
print('Begin')
from  cal  import  x , add , mul , c1  #   Import  members   x , add , mul  and  class  c1  of  cal  module  and  also  statements  of  cal  module
print(x)  #  100 : Object  'x'   imported  from  cal   module  
#print(y) #  Error :  Current  module  does  not  have  object  'y'  
#print(cal . x)  #  Cannot  use  cal  module  as  it  is  not  imported
print(add(10 , 7))  #  17 : Executes  add()  function  imported  from  cal  module  
#print(sub(10 , 7))  #  Error :  Current  module  does  not  have  function  sub()
print(mul(10 , 7))  #  70 : Executes  mul()  function  imported   from  cal  module  
#print(div(10 , 7))  #  Error :  Current  module  does  not  have  function  div()
a = c1() #  Creates  mod1 . c1  class  object
a . m1()  #  Executes  method  m1  of  mod1 . c1  class  as   'a'  is  mod1 . c1  class  object

'''
Begin
100
17
70
m1  method
'''
