#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #   (1 , 2 , 3)  <space>  Address  of  3-element  tuple  
a += b  #   Concatenates  tuples  'a'  and  'b'  to  form  a  new  tuple  and  Modifies  ref  'a'  to  a  new  tuple  of  6  elements
print(a , id(a)) #  (1 , 2 , 3 , 4 , 5 , 6)  <space>  Address  of  6-element  tuple  



'''
a = (1 , 2 , 3)
b = (4 , 5 , 6)
a += b
What  does  a += b  do ?  --->  Concatenates  tuples  'a'  and  'b'  to  form  a  new  tuple
What  is  modified  (reference  (or)  tuple) ?  --->  Reference
Is  id(a)  same  as  before  (or)  modified ? --->  Modified  as  ref  'a'  points  to  a  new  tuple
'''
