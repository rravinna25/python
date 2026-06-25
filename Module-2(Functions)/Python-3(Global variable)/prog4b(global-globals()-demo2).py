# Find outputs (Home  work)
def  f1():
	global   a #  Treats  'a'  as  Gv
	a = 10  #  Creates  Gv  with  value  10
	print(a) #  Gv  i.e. 10
	a = 20 #  Modifies  Gv  to  20
def  f2():
	global  a  #  Treats  'a'  as  Gv
	print(a) #  Gv  i.e. 20
	a = 30  #  Modifies  Gv  to  30
def  f3():
	print(a) #  Gv  i.e. 30
	globals()['a'] = 40  #  Modifies  Gv  to  40
# End  of  the  function
f1()
f2()
f3()
print(a) #  Gv  i.e. 40


'''
10
20
30
40
'''
