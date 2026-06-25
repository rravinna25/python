# Find  outputs  (Home  work)
list = [25 , 10.8 , 'Hyd' , True]
#a , b , c , d , e = list # Error :  List  should  have  5  elements  as  5  objects  are  on  leftside
a , b , *c , d , e = list  #  Unpacks  list  into  5 elements
print('a : ' , a) #a : 25
print('b : ' , b) #b : 10.8
print('c : ' , c) #c : []
print('d : ' , d) #d : Hyd
print('e : ' , e) #e : True
#a , b , *c , d , e , f = list  # Error :  List  should  have  at  least  5  elements  as   6  objects  are  on  leftside
