# Find  outputs  (Home  work)
a = b = c = 25  #  References  a , b  and  c  point  to  object  25
print(a , b , c)  #  25  <space>  25  <space>  25
del   a  #  Deletes  ref  'a'  but  not  object  as  there  are  2  more  references (i.e. b  and  c)  to  object  25
print(b , c)  #  25  <space>  25
#print(a)  #  Error :  Ref  'a'  does  not  exist
del   b  #  Deletes  ref  'b'  but  not  object  as  there  is  one  more  reference(i.e. c)  to  object  25
print(c) #  25
#print(b)  #  Error :  Ref  'b'  does  not  exist
del   c  #  Deletes  ref  'c'  and  pvm  deletes  object  as  there  are  no  more  references   to  the  object
#print(c)  #  Error :  Ref  'c'  does  not  exist
