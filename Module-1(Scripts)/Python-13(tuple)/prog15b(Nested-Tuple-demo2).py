# Find  outputs  (Home  work)
a = ((10 , 20 , 30),)  #  Nested  tuple  due  to  comma
print(a[0]) #    Inner  tuple  (10,20,30)
print(*a) #  Unpacks  tuple  'a'  to obtain   inner  tuple  (10 , 20 , 30)
print(a[0][0]) #  (10 , 20 , 30)[0]  is  10
print(a[0][1]) #  (10 , 20 , 30)[1]  is  20
print(a[0][2]) #  (10 , 20 , 30)[2]  is  30
b = ((),)  #   Nested  tuple
print(b[0]) #  Inner  tuple  ()
print( *b) # Unpacks  tuple  'b'  to obtain   inner  tuple  ()
