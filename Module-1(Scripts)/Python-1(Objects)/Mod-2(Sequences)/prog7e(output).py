# Find  outputs
#a = { [ ] : 25} # Error :  List  can  not  be  the  key  as  list  is  a  mutable  object  
b = { ( ) : 25}  #  Valid :  Tuple  can  be  the  key  as  tuple  is   immutable  object  
print(b) #   { ( ) : 25}
#c = { { } : 25} # Error :  dict  can  not  be  the  key  as  dict  is  a  mutable  object  
d = {'Ramesh' : [9948250500, 9848565090, 9440250404]} #  Valid :  str  can  be  the  key  as  str  is   immutable  object  
print(d)  #  {'Ramesh' : [9948250500, 9848565090, 9440250404]}   
print(len(d))  #  1
#e = {set() : 10.8}  # Error :  Set  can  not  be  the  key  as  set  is  a  mutable  object  
