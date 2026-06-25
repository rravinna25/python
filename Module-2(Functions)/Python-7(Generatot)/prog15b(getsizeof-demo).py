# Find  outputs
import  sys
list = [x * x   for   x   in    range(10000)]  #  Creates  a  list  of  10000 elements
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))  #  Creates  an  empty  generator  object
print(sys . getsizeof(list))  #  size  of  list  with  10000  elements  :   85176  bytes
print(sys . getsizeof(gen))   #  size  of  empty  generator :  200  bytes


'''
85176  bytes  of  memory  is  needed  for  storing   10000  elements  in  the  list
but  negligible  memory  is   needed  to  create  a  generator  object
'''
