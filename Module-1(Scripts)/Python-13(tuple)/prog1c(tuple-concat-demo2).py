#  Find  outputs
a = (1 , 2 , 3)
b = (4 , 5 , 6)
print(a , id(a)) #   (1 , 2 , 3)  <space>  Address  of  3-element  tuple  (1 , 2 ,  3)
a += b  #   Concatenates  tuples  'a'  and  'b'  to  form  a  new  tuple  and  Modifies  ref  'a'  to  a  new  tuple  of  6  elements
print(a , id(a)) #  (1 , 2 , 3 , 4 , 5 , 6)  <space>  Address  of  6-element  tuple  (1 , 2 ,  3 , 4 , 5 , 6)


'''
a += b
a = a + b
What  is  the  difference  between  the  two  statements ?  --->  Nothing
'''
