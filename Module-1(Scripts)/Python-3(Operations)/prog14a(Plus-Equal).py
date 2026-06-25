#  Find  outputs
a = 7
print(a , id(a))   #  7  <space> Address  of  object  7
a += 5 #  a = a + (5)   --->  a = 7 + (5) = 12
print(a , id(a))   #   12 <space> Address  of  object  12


'''
1) What  is  the  expansion  of  LHS  op=  RHS ?   --->  LHS  =  LHS  op  (RHS)  where  op  is  any  operator

2) a = 7
    What  does  a += 5  do ?  --->  Modifies  ref  'a'  to  object  12

3) a = 7
    a += 5
	Why  is  object  'a'  not  modified ?  --->  Since  int  object  is  immutable 
'''
