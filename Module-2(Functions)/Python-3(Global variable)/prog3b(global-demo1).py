# global  keyword  demo  program (Home  work)
def    f1():
	x = 20   #  Creates  Lv  with  value  20
	print(x)  # Lv  i.e. 20
def   f2():
	global  x  #  Treats  'x'  as  Gv
	x = 30 # Modifies  Gv  to  30
	print(x) # Gv  i.e.  30
	x += 1  #  Increments  Gv  by  1  i.e. 31
def   f3():
	global  y   #  Treats  'y'  as  Gv
	y = 40  #  Creates  Gv   with  value  40
	print(y) #  Gv  i.e. 40
	y += 1   #  Increments  Gv  by  1  i.e.  41
def   f4():
	x = 50  #  Creates  Lv  with  value  50
	#global   x # Error :  'x'  can  not  be  treated  as  Gv  as  Lv  'x'  already  exists
#  Lv  'x'  is  lost
x = 10  #  Creates  Gv  with  value  10
print(x)  #  Gv  i.e.  10
x += 1 #  Increments  Gv  by  1  i.e. 11
f1()
print(x)  #  Gv  i.e.  11
f2()
print(x) # Gv  i.e.  31
x += 1  #  Increments  Gv  by  1  i.e. 32
f3()
print(y)  #  Gv  i.e.  41
f4()
print(x)  #  Gv  i.e.  32


'''
10
20
11
30
31
40
41
32
'''
