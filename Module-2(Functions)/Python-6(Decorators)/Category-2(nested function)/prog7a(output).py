# Find  outputs(Home  work)
def  outer():
	def  inner():
		#nonlocal  x  #  Error :  outer()  function  does  not  have  variable  'x'
		x = 20  #  Creates  Lv  of  inner() function  with  value  20
		print(x)  #   Lv  of  inner() function  i.e.  20
	# Lv  of  inner  function  is  lost
	inner() #  Executes  inner()  function
	#print(x)  #  Error :   outer()  function  does  not  have  variable  'x'
#  Nothing  is  lost  as  there  is  no  Lv  in  outer  function
outer()  #  Executes  outer()  function
#print(x)  #  Error:  Gv  'x'  does  not  exist



'''
1) Can  inner()  function  use  nonlocal  keyword  without  a  Lv  in  outer()  function ?  --->  No

2) Can  outer()  function  use  LV  of  inner()  function ?  --->  No
    Can  inner()  function  use  LV  of  outer()  function ?  --->	Yes  with  nonlocal  keyword
'''
