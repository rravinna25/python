#pow()  function  demo  program
import  math
print(math . pow(2 , 3))  #  2 ^ 3 = 8.0
print(math . pow(-2 , -3))  # -2 ^ -3
print(math . pow(10 , -2)) #  10 ^ -2 = 0.01
print(math . pow(4 , math . pow(3 , 2))) #   4 ^ 3 ^ 2 = 4 ^ 9


'''
pow()  function
-----------------
1) What  does  pow(a , b)  do ?  ---> Returns  a ^ b

2) What  is  the  result  of  pow(5 , 2) ?  --->  25.0  but  not  25

3) In  other  words,  pow()  function  returns  float  result

4) Where  is  pow()  function  defined ?  ---> In  math  module

5) What  are  the  two  ways  to  obtain  a ^ b ? --->  a ** b   and   math . pow(a , b)

6) Can  a  module  be  used  without  import ?  --->  No

7) What  is  the  pre-requisite  to  use  a  module ?  --->  It  needs  to  be  imported

8) What  is  a  nested  call ?  --->  A  function  call  inside  another  function  call
												      Eg:  math . pow(a , math . pow(b , c))

9) math . pow(a , math . pow(b , c))
    Which  call  is  executed  first ?  ---> Inner  call  is  executed  before  outer  call
'''
