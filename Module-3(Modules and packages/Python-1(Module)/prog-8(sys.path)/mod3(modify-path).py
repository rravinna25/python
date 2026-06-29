# Save  rr.py  module  in  c:\\sairam  folder  before  the  program  is  executed  (Home  work)
import  sys  #  Automatically  initializes  sys . path  to   6  directories
print(len(sys . path))  #  6 :  Number  of  directories  (or)  folders  in  sys.path  
sys . path . append('c:\\sairam') #  Appends  c:\sairam  folder  to  sys.path
print(len(sys . path))  #  7 : Number  of  directories  (or)  folders  in  sys.path  
import  rr  #  Imports  sample  module  from  c:\sairam  folder  which  is  present  in  sys.path
print(rr . x)  #  25 : Object  'x'  of  sample   module  which  is  in  c:\sairam  folder
rr . f1()  #  Executes  function  f1()  of  sample  module  which  is  in  c:\sairam  folder
a = rr . c1()  #  Creates  sample . c1  class  object
a . m1()  #  Executes  method  m1()  of  sample . c1  class  which  is  in  c:\sairam  folder
# sys . path  is  lost
