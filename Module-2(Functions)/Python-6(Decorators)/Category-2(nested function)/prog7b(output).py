# Find  outputs(Home  work)
def  outer():
	def  inner():
		global   x  #  Treats  'x'  as  Gv
		x = 20 #  Creates  Gv  with  value  20
		print(x)#  20 : Gv 
		x = x + 5  #  Modifies  Gv  to  25
	# Nothing  is  lost  becoz  inner()  function  does  not  have  Lv  
	inner()  #  Executes  inner()  function
	print(x) #  25 : Gv  
# Nothing  is  lost  becoz  outer()  function  does  not  have  Lv  
outer()  #  Executes  outer()  function
print(x)  #  25 : Gv  


'''
20
25
25


1) def  f1():
	     global  x
   Can  function  use  global  keyword  without  GV  in  the  program  ?  --->  Yes

2) def  f1():
	     def  f2():
		       nonlocal  x
    Can  inner  function  use  nonlocal  keyword  without  a  local  variable  in  outer()  function  ?  ---> No
'''
