# Find outputs (Home  work)
def  f1():
	global  a  #  Treats  'a'  as  Gv
	a = 20  # Modifies  Gv  to  20
	print(a)  #  Gv  i.e.  20
	print(globals()['a'])  #  Gv  i.e.  20
	a = 30  # Modifies  Gv  to  30
# End of the function
a = 10   #  Creates  Gv  with  value  10
print(a)  # Gv  i.e.  10
f1()
print(a) #  Gv  i.e.  30


'''
10
20
20
30
'''
