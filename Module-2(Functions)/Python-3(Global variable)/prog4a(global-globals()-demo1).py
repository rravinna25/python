# Find  outputs(Home  work)
def  f1():
	global  a  #  Treats  'a'  as   Gv
	#print(a) # Error :  Gv  'a' does  not  exist
	a = 10  #  Creates  Gv  with  value  10
	print(globals()['a']) #  Gv  i.e. 10
	a = 20  #  Modifies  Gv  to  20
	print(a) # Gv  i.e. 20
	a = 30  #  Modifies  Gv  to  30
def  f2():
	print(a) #  Gv  i.e. 30
# End  of   f2   function
f1()
f2()
print(a)  # Gv  i.e. 30


'''
10
20
30
30


Does  global  x  creates  a  global  variable  ?  --->  No  and  it  requests  function  to  treat   variable  'x'  as  global
'''
