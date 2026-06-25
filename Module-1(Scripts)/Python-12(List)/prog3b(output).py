# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]  #   Ref  'a'  points  to  3-element  list
b = [4 , 5 , 6]
print(a , id(a))  #   [1 , 2 , 3]  <space>  Address  of   3-element  list
a += b  #  Appends  elements  of  list  'b'  to  list  'a'
print(a , id(a))  #   [1 , 2 , 3 , 4 , 5 , 6]  <space>  Same  address  


'''
What  does  a += b ?  --->  Concatenates  elements  of  list  'b'  to  list  'a'
'''