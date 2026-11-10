# Find  outputs
import   sys
class   c1:
        pass
# End  of  the  class
a = b = c = d = c1()  #   References  a , b , c  and  d  point  to  c1  class  object
print(sys . getrefcount(b)) #  Number  of  references  to  object   'b'  i.e.  4 + 1 = 5
print(sys . getrefcount(c1())) #  Number  of  references  to  c1  class  object   i.e.  0 + 1 = 1
print(sys . getrefcount(25)) # Number  of  references  to  int  object  25  which  cannot  be  predicted  as  int  is  immutable  and  reusable  object
print(sys . getrefcount([10 , 20 , 15 , 18])) #  Number  of  references  to   list  object   i.e.  0 + 1 = 1
print(sys . getrefcount(10.8)) # Number  of  references  to  float  object  10.8  which  cannot  be  predicted  as  float   is  immutable  and  reusable  object
print(sys . getrefcount({10 , 20 , 15 , 18})) #  Number  of  references  to  set  object   i.e.  0 + 1 = 1
print(sys . getrefcount('Hyd'))  # Number  of  references  to  str  object  'Hyd'   which  cannot  be  predicted  as  str  is  immutable  and  reusable  object
print(sys . getrefcount({10 : 20 , 30 : 40})) #  Number  of  references  to  dict  object   i.e.  0 + 1 = 1
print(sys . getrefcount((10 , 20 , 30 , 40))) # Number  of  references  to  tuple  which  cannot  be  predicted  as  tuple  is  immutable  and  reusable  object


'''
1) Which  objects  are  reusable ?  ---> All  immutable  objects  except  range  object

2) Which  objects  are  not  reusable ?  --->  All  mutable  objects  and  range  object
'''
