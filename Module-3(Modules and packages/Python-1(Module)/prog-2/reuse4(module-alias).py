# Module  alias
print('Begin')
import  cal  as  c  #   Imports  cal  module  with   another  name  'c'
print(c . x)  #  Object  'x'  of  module  'c'  i.e.  100
print(c . y)  #  Object  'y'  of  module  'c'  i.e.  200
print(c . add(10 , 7)) #  Executes  add()  function  of  module  'c'  i.e.  17
print(c . sub(10 , 7)) #  Executes  sub()  function  of  module  'c'  i.e.  3
print(c . mul(10 , 7))  #  Executes  mul()  function  of  module  'c'  i.e.  70
print(c . div(10 , 7))  #  Executes  div()  function  of  module  'c'  i.e.  1.42
a = c . c1()  #  Creates  c . c1  class  object
a . m1() #  Executes  method  m1()  c . c1  class
#print(cal . x)  #   Error :  Cannot  use  cal  module  as  it  is  not  imported
#from  math  as   m  import  *  #  Error :  Cannot  do  module   alias   as  module  is  not  being  imported



'''
1) from  math  as   m  import  *
    Why  is  module  alias  not  permitted ?  --->  Since  module  is  not  being  imported

2) How  to  perform  module  alias ?  ---> With  import  statement  and  as  keyword
																 i.e. import  math  as  m

3) How  to  perform  member  alias ?  ---> With  from  statement  and  as  keyword
																   i.e.  from  module  import  member  as  m
'''
