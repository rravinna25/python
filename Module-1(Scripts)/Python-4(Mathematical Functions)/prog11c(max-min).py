#  max()  and  min()   functions  demo  program
from  builtins  import   max , min  #  Optional :  max()  and  min()  functions  are  automatically  imported  from  builtins  module
print(max(10.8 , 20.6)) # 20.6
print(min(10.8 , 20.6 , 5.9 , 12.3)) # 5.9
print(max(25 , 10.8)) # 25
import  builtins  #  Mandatory :  Not  imported  automatically
print(builtins . max(10 , 20 , 30)) # 30
print(builtins . min(10 , 20 , 15 , 5 , 12)) # 5


'''
1) How  many  arguments  can  max()  and  min()  functions  take  ?  --->
																			Any  number  of  arguments  becoz  they  are   var-arg  functions
																			
2) Is  print  a  var-arg  function ?  ---> Yes																			
'''
