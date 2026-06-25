# Find  outputs  
a = [10 , 20 , 30]  #  Ref  'a'  points  to  3-element  list
print(a , id(a))  #  [10 , 20 , 30]  <space>  Address  of  list
a += [40 , 50 , 60]  #  Appends  elements  of  list  [40 , 50 , 60]  to  list  'a'   i.e. List  is  modified
print(a , id(a))  #  [10 , 20 , 30 , 40 , 50 , 60]  <space>  Same  address  
a = [10 , 20 , 30]  #  Ref  'a'  points  to  3-element  list
print(a , id(a))  #  [10 , 20 , 30]  <space>  Address  of  list  [10 , 20 , 30]
a = [40 , 50 , 60]  #  Modifies  ref  'a'  to  another  list 
print(a , id(a))  #   [40 , 50 , 60]  <space>  Address  of  list   [40 , 50 ,  60]
