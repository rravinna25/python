# Find  outputs (Home  work)
def   f1():
	a = 20 #  Creates  Lv  with  value  20
	print(a) #  Lv  i.e. 20
def  f2():
	#print(a) # Error :  Gv  can  not  be  printed  as  Lv  'a'  is  created  in  the  subsequent statement 
	#a += 1 #  a = a +  1   ---> Error  :  Lv  'a'  is  used  on  right  side  without  initialization
	pass
# End of the function
a = 10  #  Creates  Gv  with  value  10
print(a) #  Gv  i.e. 10
f1()
a += 1 #  Modifies  Gv  to  11
f2()
print(a) #  Gv  i.e. 11


'''
10
20
11


1) Python  function  cannot   use  global  variable  for  some  time  and  local  variable  subsequentlt

2) Why  is  pass  used  in  function  f2() ?  --->  Since  function  does  not   have  any  statements
'''
