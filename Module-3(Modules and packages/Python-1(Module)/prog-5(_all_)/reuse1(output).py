#  Find  outputs
from  calc  import  * #  Imports  those  members  which  are  in   __all__  list  of  calc  module  i.e.  add() ,  object  'x'  , mul()  and  class  c1
print(x) #  Object  'x'  which  is  imported  from  calc  module  i.e.  100
#print(y) #  Error :  Neither  current  module  has  object  'y'  nor  member  'y'  is  imported  from  calc  module
print(add(10 , 7))  #  Executes  add()  function  which  is  imported  from  calc  module  i.e.  17
#print(sub(10 , 7))  #  Error :  Neither  current  module  has  function  sub()  nor  sub()  function  is  imported  from  calc  module
print(mul(10 , 7))   #  Executes  mul()  function  which  is  imported  from  calc  module  i.e.  70
#print(div(10 , 7))    #  Error :  Neither  current  module  has  function  div()  nor  div()  function  is  imported  from  calc  module
a = c1() #  Creates  imported  class  (i.e.  c1  from  calc)  object
a . m1()  #  Executes  method  of  imported  class  c1  from  calc  module

'''
100
17
70
m1  method
'''
