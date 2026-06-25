# Find outputs (Home work)
a = 'Hyd'   #  Ref  'a'  points  to  object  'Hyd'
b = 'Hyd'   #  Ref  'b'  points  to  same  object  'Hyd'
print(a  is  b) # True  :  References  'a'  and  'b'  point  to  same  object  'Hyd'
print(a  is  not  b) # False
print(a == b) # True  : Objects  'a'  and 'b' have  same  string  'Hyd'
print()
x = [1 , 2 , 3 , 4]  # Ref  'x'  points  to  list
y = [1 , 2 , 3 , 4]  #  Ref  'y'  points  to  a  different  list  as  list  is  mutable  and  not  reusable
print(x  is  y) # False  :  References  'x'  and  'y'  point  to  different  lists
print(x  is  not  y) # True
print(x == y) # True :  Lists  'x'  and 'y'  have  same  elements
print()
m = (1 , 2 , 3 , 4)  # Ref  'm'  points  to   tuple
n = (1 , 2 , 3 , 4)  #  Ref  'n'  points  to  same  tuple
print(m  is  n) # True  :  References  'm'  and  'n'  point  to  same  tuple
print(m  is  not  n) # False
print(m == n) # True  :  Tuples  'm'  and 'n'  have  same  elements
