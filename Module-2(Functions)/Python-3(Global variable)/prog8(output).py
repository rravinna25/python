# Find outputs (Home  work)
def  f1():
	a = 20  #  Creates  Lv  with  value  20
	#global   a # Error :  'a'  can  not  be  treated  as  Gv  as  Lv   already  exists
	print(a) #  Lv  i.e. 20
	print(globals()['a']) #  Gv  i.e.  11
	a = 30  #  Modifies  Lv  to  30
	globals()['a'] = 40  #  Modifies  Gv  to  40
#  Lv  'a'  is  lost
a = 10  #  Creates   Gv  with  value  10
print(a) #  Gv  i.e. 10
a += 1 #  Modifies  Gv  to  11
f1()
print(a) #  Gv  i.e.  40


'''
10
20
11
40
'''
