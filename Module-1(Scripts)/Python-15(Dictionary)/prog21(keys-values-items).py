#  Find  outputs  (Home  work)
a = {10 : 'Rama' , 20 : 'Sita' , 15 : 'Rajesh'}
x , y , z = a . keys()  #  Unpacks  the  list  in  dict_keys   object  to  3  elements
print(x) # 10
print(y) # 20
print(z) # 15
print()
x , y , z = a . values() #  Unpacks  the  list  in  dict_values  object  to  3  elements
print(x) # Rama
print(y) # Sita
print(z) # Rajesh
print()
x , y ,  z = a . items()  #  Unpacks  the  list  in  dict_items   object  to  3  tuples
print(x) # (10,'Rama')
print(y) # (20,'Sita')
print(z) # (15,'Rajesh')
print()
(rno1 , sname1) , (rno2 , sname2) , (rno3 , sname3) = a . items()  #  Unpacks  the  list  in  dict_items   object  to  6   elements
print(rno1 , sname1) # 10 <space> Rama
print(rno2 , sname2) # 20 <space> Sita
print(rno3 , sname3) # 15 <space> Rajesh


'''
x , y , z = a . keys()  is  same  as  what ?  --->  x , y , z = a
'''
