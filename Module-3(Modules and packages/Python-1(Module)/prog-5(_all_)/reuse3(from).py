#  Find  outputs
from  calc  import  y , sub , mul  #  Imports  object  'y' , sub()  function and  class  c1  (__all__  list  is  ignored)
#print(x) #  Error :  Current  module  does  not  have  object  'x'  and  also  'x'  is  not  imported  from  cal  module
print(y) #  200 : Object  'y'  imported  from  calc  module 
#print(add(10 , 7)) #  Error :  Current  module  does  not  have  function  add()  and  also  add()  function  is  not  imported  from  cal  module
print(sub(10 , 7))  #  3 : Executes  sub()  function  imported  from calc  module  
print(mul(10 , 7))  #  70 : Executes   mul()  function  imported  from calc  module  
#print(div(10 , 7)) # Error :  Current  module  does  not  have  function  div()  and  also  div()  function  is  not  imported  from  cal  module
#a = c1() #  Error :  Current  module  does  not  have  class  c1  and  also  class  c1  is  not  imported  from  cal  module



'''
from  calc  import   y , sub , mul
Why  are  x ,  add , mul  and  c1  not  imported  even  though  they  are  in  __all__  list ?  --->
																													Since  *  is  not  being  used  in  from  statement
'''
