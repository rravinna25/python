#  Find  outputs (Home  work)
class  c1:
        pass
# End  of  class
a = c1()  #  Creates  an  empty c1  class  object
print(a . __dict__) # { }
a . x = 10  # Adds  variable  'x'  to  object  'a'  with  value  10
print(a . __dict__) # {'x' : 10}
a . y = 20  # Adds  variable  'y'  to  object  'a'  with  value   20
print(a . __dict__) # {'x' : 10 , 'y' : 20}
a . x = 30 #  Modifies  a . x  to  30
print(a . __dict__) # {'x' : 30 , 'y' : 20}
a . y = 40  #  Modifies  a . y  to  40
print(a . __dict__) # {'x' : 30 , 'y' : 40}
del  a . x  #   Removes  variable  'x'  from   object  'a'
print(a . __dict__) # {'y' : 40}
del  a . y  #   Removes  variable  'y'  from   object  'a'
print(a . __dict__) # {}
del   a  #  Deletes  object  'a'
#print(a . __dict__) #  Error :   Object  'a'   does  not  exist
