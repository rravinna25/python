# Find  outputs (Home  work)
def   f1():
	a = 20 #  Creates  Lv  with  value  20
	print(a) #  Lv  i.e.  20
	a += 1  #  Increments  Lv  by  1  i.e.  a  is  11
#  Lv  'a'  is  lost
a = 10 #  Creates  Gv  with  value  10
print(a) # Global variable i.e. 10
a += 1 #  Increments  Gv  by  1  i.e.  a  is  11
f1()
print(a) #  Gv  i.e.  11
#  Gv  'a'  is  lost


'''
10
20
11


1) Can  a  function  use  LV  of  a  different  function ?  --->  No  becoz  it  is  not  visible

2) Can  statements  outside  the  function  use  LV  of  the  function ?  ---  No  becoz  it  is  not  visible

3) Which  variable  can  be  used  by  statements  outside  the  function  ?  --->  Only  global  variable
'''
