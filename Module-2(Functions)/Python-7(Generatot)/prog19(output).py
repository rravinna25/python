#  Find  outputs (Home  work)
def   f1():
	yield    1
	yield    2
	yield    3
# End  of  generator
g =  f1()   # Creates  an  empty  generator  object
#print(len(g)) # Error :  len()  function  expects  sequnence  but  generator  is  passed
#print(g * 3) # Error : Generator  object  can  not be  repeated  as  it  is  an  empty  object
#print(g[0]) #  Error :  Generator  object  is  not  indexed  as  it  is  an  empty  object
#print(g[1 : 3])  #  Error : Generator  object  can  not  be  sliced  as  it  does  not  have  indexes
print(*g) #  Unpacks  generator  object  to  1 <space> 2 <space> 3
