# How  to  use  members  of  cal  module  with  import  statement ?  (Home  work)
print('Begin')
import  cal  #  Imports  cal  moudle  and  all  the  statements  of  cal  module
print(cal . x) #  Object  'x'  of  cal   module  i.e.  100
print(cal . y)  #  Object  'y'  of  cal   module  i.e.  200
#print(x)  #  Error :  Current  module  does  not  have  object  'x'  
print(cal . add(10 , 7))  #  Executes  add()  function  of  cal  module  i.e.  17
print(cal . sub(10 , 7))  #  Executes  sub()  function  of  cal  module  i.e.  3
print(cal . mul(10 , 7))  #  Executes  mul()  function  of  cal  module  i.e.  70
print(cal . div(10 , 7))  #  Executes  div()  function  of  cal  module  i.e.  1.42
#print(add(cal . x , cal . y))  #  Error :  Current  module  does  not  have  add()  function 
a = cal . c1()  #   Creates  cal . c1  class  object
a . m1()  #  Executes  m1()  method  of  cal . c1  class  as  'a'  is  cal . c1  class  object
#b = c1()  #  Error :  Current  module  does  not  have  class  c1 
#cal . c1 . m1() #   Error :  Method  can  not  be  called  thru  classname
#m1()  #  Error :  Current  module  does  not  have  function  m1()


'''
1) What  is  the  syntax  to  create  an  object ?  --->  object =  classname()

2) How  to  call  method  of  a  class ?  ---> object . method()

3) Is  classname . method()  valid ?  --->  No  becoz  method  should  be  called  wrt  object  but  not  thru  classname

4) Is  method()  valid ?  --->  No  becoz  method  can  not  be  called  directly  without  object
'''
