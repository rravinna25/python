# Find  outputs
all = lambda  a , b :  (a + b ,  a - b , a * b , a / b)  #  Ref  all  points  to  lambda  function
x = all(10 , 7)  # Executes  lambda  function  with  a = 10 ,  b = 7  which  returns  a   tuple   i.e. (17 , 3 , 70 , 1.42)
print(type(x)) # <class 'tuple'>
print(x) #(17 , 3 , 70 , 1.42857)
p , q , r , s = all(9 , 2) # Executes  lambda  function  with  a = 9 ,  b = 2  which  returns  a  tuple  (11 , 7 , 18 , 4.5)  and  is  unpacked
print(p) # 11
print(q) # 7
print(r) # 18
print(s) # 4.5
