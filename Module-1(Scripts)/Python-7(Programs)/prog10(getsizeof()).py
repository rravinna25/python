#  getsizeof()   function  demo  program
import  sys
print(sys . getsizeof(10000000))  #  size  of int  object  in  terms  of  bytes
print(sys . getsizeof(10.8))   #  size  of  float   object  in  terms  of  bytes
print(sys . getsizeof(3 + 4j))   #  size  of  complex   object  in  terms  of  bytes
print(sys . getsizeof('Rama  Rao'))   #  size  of  str  object  in  terms  of  bytes
print(sys . getsizeof(True))   #  size  of   bool  object  in  terms  of  bytes
print(sys . getsizeof(None))   #  size  of  NoneType  object  in  terms  of  bytes
print(sys . getsizeof([10 , 20 , 15 , 18]))   #  size  of   list  in  terms  of  bytes
#print(getsizeof(()))   #  Error  :   Current  module  does  not  have   getsizeof()  function


'''
getsizeof()  function
------------------------
1) What  does  getsizeof(object)  do ?  ---> Returns  size  of  any  python  object  in  the  form  of  bytes

2) Where  is  getsizeof()  function  defined ?  --->  In  sys  module
'''
