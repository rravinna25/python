#  Find  outputs
a = 25   # Ref  'a'  points  to  object  25
print(id(a)) #  Address  of object  25  (may be   1000)
a = 35  #  Modifies   ref  'a'   to  object   35
print(id(a))  #  Address  of object  35  (may be   2000)



'''
1) a = 25
    a = 35
	What  is  modified  when  a  = 35   is  executed  ?  --->  Reference  but  not  object

2) Why  is  object  not  modified ?  --->  Since  int  object  is  immutable

3) Therefore  25  in  object  'a'  is  not  replaced  with  35
'''
