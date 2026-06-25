# Tricky  program
#  Find  outputs
a = [1 , 2 , 3]  #   Ref  'a'  points  to  3-element  list
b = [4 , 5 , 6]
print(a , id(a))  #   [1 , 2 , 3]  <space>  Address  of  6-element  list
a  = a + b  #  Modifies  ref  'a'  to  a  new  list  of  6-elements
print(a , id(a))  #   [1 , 2 , 3 , 4 , 5 , 6]  <space>  Address  of  6-element  list


'''
1) What  does  a = a + b  do ?  --->  Modifies  reference  'a'  to  a  new  list  of  6-elements

2) a += b
    a =  a + b
	What  is  the  difference  between  the  two  statements ? --->  a += b  modifies  list  'a'  but  a = a + b  modifies  ref  'a'
'''
