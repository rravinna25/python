#  floor()  and  ceil()  functions  demo  program
import  math
print(math . floor(10.8)) #   Nearest  Prev  integer  10
print(math . ceil(10.8)) #  Nearest  next  integer  11
print(math . floor(25.0)) #  25  due  to  .0
print(math . ceil(25.0))   #  25  due  to  .0
print(math . floor(-3.5)) #   Prev   integer  -4
print(math . ceil(-3.5)) #   Next  integer  -3
print(math . floor(-9.0)) #  -9  due  to  .0
print(math . ceil(-9.0)) #  -9  due  to  .0
print(math . floor(25.1)) # 25
print(math . ceil(25.1)) #26
#print(floor(3.5)) # Error :  Current  module  does  not  have  floor()  function
#print(ceil(3.5)) #  Error :  Current  module  does  not  have  ceil()  function


'''
floor()  and  ceil()  functions
--------------------------------
1) What  does  floor(x)  do ?  --->  Returns  nearest  previous  integer  of  'x'

2) What  does  ceil(x)  do ?  --->  Returns  nearest  next  integer  of  'x'

3) Where  are   floor()  and  ceil()  functions  defined ?  ---> In  math  module
'''
