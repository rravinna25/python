# Find  outputs (Home  work)
a = 25.7  #  Ref  'a'  points  to  object  25.7
print(id(a)) #   Address  of  object   25.7  (may  be  1000)
print(a) #  25.7
a = 35.6  #   Modifies  ref  'a'   to   object  35.6
print(id(a)) #   Address  of  object  35.6   (may  be  2000)
print(a) #  35.6
b = True #  Ref  'b'  points  to  object  True
print(id(b)) #   Address  of  object   True   (may  be  3000)
b = False #  Modifies  ref  'b'  to   object  False
print(id(b))  #   Address  of  object  False   (may  be  4000)
c = None #  Ref  'c'  points  to  object  None
print(id(c)) #   Address  of  object   None  (may  be  5000)
c = None #   Nothing  is  modified  :  Ref  'c'  already  points  to  None
print(id(c))  #   Address  of  object   None  (5000)
