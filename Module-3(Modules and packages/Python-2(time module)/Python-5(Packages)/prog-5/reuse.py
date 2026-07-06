# Save  in  any  file  of  cwd
from  p1   import  *   #  Imports  mod1  and  mod3  becoz  they  are  in  __all__  list  which  is  in  p1 . __init__  module
mod1 . f1()  #   Executes  function  f1()  of  p1 . mod1
mod3 . f1()   #  Executes  function  f1()  of  p1 . mod3
#mod2 . f1()  #   Error :  mod2  is  not  imported  from  package  p1  as  it  is  not  in  __all__  list
