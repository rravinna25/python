# Find  outputs  (Home  work)
a = [10 , (20 , 30 , 40) , 50 , 60]   #   Tuple  in  list
#a[1][0] = 70 #  (20 , 30 , 40)[0] = 70  ---> Error :  Tuple  element can  not  be  modified  as tuple is immutable
print(a) # [10 , (20 , 30 , 40) , 50 , 60]
a[1] = [80 , 90] #  Modifies  2nd  element  of  list  to  [80,90]
print(a) # [10 , [80 , 90] , 50 , 60]
