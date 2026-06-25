#  Find   outputs(Home  work)
def  outer():
	x = 10 #  Lv  of  outer  function
	def  inner():
		global   x  #  Treats  'x'  as  Gv
		x = 20  #  Creates  GV  with  value  20
		print(x) #  Gv  i.e.  20
		x += 5  #  Modifies  Gv  to  25
	# Nothing  is  lost  becoz  inner  function  does  not  have  Lv  
	print(x)  #  Lv  of  outer  function  i.e.  10
	x += 5  #  Modifies  Lv  of  outer  function  to  15
	inner() #  Executes  inner()  function
	print(x)   #  Lv  of  outer  function  i.e.  15
# Lv  of  outer  function  is  lost
outer()  #  Executes  outer()  function
print(x) #  Gv  i.e. 25


'''
10
20
15
25
'''
