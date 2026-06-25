#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'  #  Multiple  assignment
print(a , b , c) #  25  <space>  10.8  <space>  Hyd
del   a , b , c  #  Deletes  all  the  3  references  and  objects
#print(a)  #  Error :  Ref  'a'  does  not  exist
#print(b)  #  Error :  Ref  'b'  does  not  exist
#print(c)   #  Error :  Ref  'c'  does  not  exist


'''
del   a , b , c
How  to  divide  the  statement  into  three  statements ?  ---> del   a
																								 del   b
																								 del   c
'''
