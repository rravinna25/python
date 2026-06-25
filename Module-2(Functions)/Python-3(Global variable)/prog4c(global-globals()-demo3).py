# Find outputs (Home  work)
def  f1():
	global   a  #  Treats  'a'  as  Gv
	a = 10  #  Creates  Gv  with  value  10
	print(a) #  Gv  i.e.  10
	a = 20  #  Modifies  Gv  to  20
def  f2():
	#print(a) # Error :  Gv  can  not  be  printed  as  Lv  'a'  is  created  in  the  following  statements
	a = 30  #  Creates  Lv  with  value   30
	print(a)  #  Lv  i.e.  30
def  f3():
	print(a) #   GV  i.e. 20
	globals()['a'] = 40  #  Modifies  Gv  to  40
# End  of  the  function
f1()
f2()
f3()
print(a)  #  Gv  i.e.  40


'''
10
30
20
40
'''


'''
1) Can  a  function  use  global  variable  when  it  does  not  have  local  variable ?  --->  Yes 
																				
2) Can  a  pyhton  function  use  global  variable  for  some  time  and  local  variable  later ?  --->  No

3) In  other  words,  python  function  can  use  either  global  variable  throughout  (or)  local  variable  throughout 
     but  not  both  (Unlike  'c'  language  function)
'''
