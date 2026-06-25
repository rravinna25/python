# sqrt()  function  demo  program
import  math
print(math . sqrt(25))  #  5.0
print(math . sqrt(10)) #   3.16
print(math . sqrt(6.25))  #  2.5
print(math . sqrt(True))  #  1.0
#print(math . sqrt(3+4j)) #  Error :   sqrt(complex-number)  can not  be  determined
print(math . sqrt(math . sqrt(256)))  #  math . sqr(16.0) = 4.0
print(math . sqrt(math . pow(3 , 4)))  #  math . sqrt(81.0) = 9.0
#print(math . sqrt(-16))  #  Error :  sqrt(-ve  number)  can  not  be  determined
#print(sqrt(49))  #  Error  :  Current  module  does  not  have  sqrt()  function


'''
sqrt()  function
-------------------
1) What  does  sqrt(x)  do ?  ---> Returns  square  root  of  'x'

2) What  is  the  result  of  sqrt(25)  ?   --->  5.0  but  not  5

3) In  general,  sqrt()  function  returns  float  result

4) Where  is  sqrt()  function  defined ?  ---> In  math  module

5) math . sqrt(x)
    Where  is  sqrt()  function  searched ?  ---> In  math  module

6) sqrt(x)
    Where  is   sqrt()  function  searched ? --->  In  current  module  (or)  program

7) Can  sqrt(-ve  value)  be  determined ?  --->  No  and  it  leads  to  error

8) math . sqrt(math . pow(x , y));
    Which  function  is  executed  first ? ---> Inner  function  is  executed  before  outer  function
'''
