# Tuple  Comprehension
g = (x * x   for   x   in   range(5)) #  Creates  an empty  generator  object
print(type(g))  #  <class  'generator'>
print(g)  #  Type  and  address  of   object  'g'
print(*g) #   Stores  0 ^ 2 , 1 ^ 2 , 2 ^ 2 , 3 ^ 2 , 4 ^ 2  in  object  'g'  ,  unpacks  object  'g'  to  5  elements  and   object  becomes  empty
t = tuple(x * x   for   x   in   range(5))  #  Converts  generator  object  to  tuple
print(t)  #  (0 , 1 , 4 , 9 , 16)
print(type(t)) #   <class  'tuple'>



'''
1) What  is  (x * x  for  x  in  range(5))  called ? --->  Generator  expression  but  not  tuple  comprehension

2) What  does  (x * x  for  x  in  range(5))  do ?  --->  Creates  an  empty  generator  object  but  not  tuple  with
														                            0  ^ 2 ,  1 ^ 2 , 2 ^ 2 , 3 ^ 2  and  4  ^ 2
'''
