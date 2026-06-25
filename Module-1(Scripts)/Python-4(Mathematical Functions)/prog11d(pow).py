# pow()  function  demo  program
from  builtins  import  pow  #  Optional  :  pow()  function  is  automatically  imported  from  builtins  module
print(pow(10 , -2)) #  10 ^ -2 = 0.01
print(pow(4 , pow(3 , 2))) # 4 ^ 3 ^ 2 =  4 ^ 9
import  builtins  #  Mandatory :  Not  imported  automatically
print(builtins . pow(2 , 3)) # 8
print(builtins . pow(-2 , -3)) #  -2 ^ -3


'''
1) Where  is  pow()  function  defined ?  --->  In  builtins  module  and  also  in  math  module

2) What  are  the  four  ways  to  obtain  a ^ b ?  --->  a ** b  ,  math . pow(a , b) ,  builtins . pow(a , b)  and  pow(a , b)

3) math . pow(a , b)
    Function  of  which  module  is  executed ?  ---> math  module

4) builtins . pow(a , b)
    Function  of  which  module  is  executed ?  --->  builtins  module
	
5) pow(a , b)
    Function  of  which  module  is  executed ?  --->  builtins  module
'''
