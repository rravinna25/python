#  Find  outputs (Home  work)
a = ((10 , 20 , 30))  #  Single  tuple  but  not  nested  tuple  as  comma  is  missing
print(a) #  Single  tuple  i.e. (10 , 20 , 30)
print(*a) #   Unpacks  tuple  'a'  to  obtain   elements  i.e.  10  <space>  20  <space>  30
b = (()) #  Single  tuple  but  not  nested  tuple  as  comma  is  missing
print(b) # ()
print(*b) # Unpacks  tuple  'b'  to  nothing  as  it  is  an  empty  tuple
