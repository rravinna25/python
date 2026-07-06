'''  (Home  work)
Save  the  following  code  in  any  file  of  cwd
How  to  use  members  of  both  the  modules
'''
from  p1 . mod1  import  x  as  x1 ,  f1  as  f11 ,  c1  as  c11  #  Imports   all  the  members  of   p1 . mod1  with  new  names
from  p1 . mod2  import  *  #  Imports   all  the  members  of  p1 . mod2
print(x1) #  Object  x  imported (with  name  x1)  from  p1 . mod1  i.e.  10
f11() #   Executes  function  f1()   imported  (with  name  f11)  from  p1 . mod1
a = c11()  #  Creates  p1 . mod1 . c1  class  object
a . m1()  #  Executes  method  m1()  of  class  c1  imported  (with  name  c11) from  p1 . mod1
print()
print()
print(x) #  Object  'x'   imported  from  p1 . mod2  i.e.  20
f1() #  Executes  function  f1()  imported  from  p1 . mod2  module
a = c1() # Creates  p1 . mod2 .  c1  class  object
a . m1() #  Executes  method  m1()  of  class  c1  imported  from  p1 . mod2  module


'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1


How  to  use  members  of  both  the  modules  without  importing  the  modules ?  --->  With  member  alias
'''
