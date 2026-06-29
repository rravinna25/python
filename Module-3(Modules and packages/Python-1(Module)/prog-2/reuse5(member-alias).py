# Member  alias
from  cal  import  x  as   k ,  add  as  sum ,  mul  as  product  ,  c1  as  c2  #  Import  members   x , add , mul  and  class  c1  of  cal  moudle  with  another  name
print(k)  #  Object  'k'  (i.e. x)  imported  from  cal   module  i.e.  100
#print(x)  #  Error :  Current  module  does  not  have  object  'x'  
print(sum(10 , 7))  #  Executes  sum()  function  (i.e. add()  function)  imported  from   cal  module  i.e.  17
print(product(10 , 7)) #  Executes  product()  function  (i.e. mul()  function)  imported  from   cal  module  i.e.  70
a = c2()  #  Creates  the  imported  class  object  i.e.  c2  class  object
a . m1()  #  Executes  method  m1()  of  the  imported  class
#print(add(10 , 7))  #  Error :  Current  module  does  not  have  function  add()
#b = c1()  #  Error  :  Current  module  does  not  have  class  c1


'''
100
17
70
m1  method
'''

# cal . py , reuse1 . py , reuse2 . py ,  reuse3 . py , reuse4 . py ,  reuse5 . py  should  be  in  same  folder  (prog2  folder)
