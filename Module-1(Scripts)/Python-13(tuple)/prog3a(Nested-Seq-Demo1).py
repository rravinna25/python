# Find  outputs  (Home  work)
a = (10 , [20 , 30 , 40] , 50 , 60) # List  in  tuple
a[1][0] = 70 #  [20 , 30 , 40][0] = 70  --->  Modifies  1st  element  of  inner  list  to  70
print(a) # (10 , [70 , 30 , 40] , 50 , 60)
#a[1] = [80 , 90] # Error :  Tuple  element  can  not  be  modified  as  tuple  is  immutable
print(a) # (10 , [70 , 30 , 40] , 50 , 60)



'''
a = (10 , [20 , 30 , 40] , 50 , 60)
Can  outer  sequence  be  modified ?   ---> No  becoz  it  is  a  tuple
Can  inner  sequence  be  modified ?   ---> Yes  becoz  it  is  a  list
'''
