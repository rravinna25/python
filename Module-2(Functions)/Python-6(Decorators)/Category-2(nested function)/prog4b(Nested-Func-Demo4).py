# Find  outputs  (Home   work)
x = 10  # Global  variable
def  outer():
	x = 20  #  Local  variable  of  outer()  function
	def   inner():
		print(x)  #  Local  variable  of  outer()  function  i.e.  20
		print(globals()['x'])  #  Gv  i.e.  10
	# Nothing  is  lost  becoz  inner  function  does  ot  have  LV
	inner()
# Lv  of  outer  function  is  lost
outer()


'''
20
10


When  can  inner  function  use  variable  of  outer()  function ?  ---> 
																		When  inner()  function  does  not  have  variable  with  same  name  
'''
