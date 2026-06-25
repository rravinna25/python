#  Find  outputs  (Home  work)
def  outer():
	x = 10  # Lv  of  outer()  function
	def  inner():
		#print(x)  #  Error :  inner()  function  does  not  have  Lv  'x' 
		nonlocal  x  #  inner  function  uses  Lv  of  outer()  function
		x = 20   #  Modifies  Lv  of  outer()  function  to  20
		print(x)  # Lv  of  outer()  function  i.e.  20
		x += 5   #  Modifies  Lv  of  outer()  function  to  25
	# Nothing  is  lost  as  there  is  no  Lv  in  inner  function
	print(x)   # Lv  of  outer()  function  i.e.  10
	x += 5 #  Modifies  Lv  of  outer()  function  to  15
	inner()  #  Executes   inner()  function
	print(x)  # Lv  of  outer()  function  i.e.  25
# Lv  of  outer  function  is  lost
outer()  #  Executes  outer()  function


'''
10
20
25
'''
