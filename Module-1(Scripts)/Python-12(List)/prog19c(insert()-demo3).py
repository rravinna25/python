#  Find  outputs (Home  work)
a = [10 , 20 , 30 , 40]
b = [50 , 60 , 70]
a . insert(2 , b)  #  Inserts  list  'b'  at  index 2  of  list  'a'
print(a) # [10 , 20 , [50 , 60 , 70] , 30 , 40]
print(len(a)) # 5
print(a[2]) # [50 , 60 , 70]
print(a[2][0]) # [50 , 60 , 70][0] is  50
print(a[2][1]) # [50 , 60 , 70][1] is  60
print(a[2][2]) # [50 , 60 , 70][2] is  70
