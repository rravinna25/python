# Find  outputs  (Home  work)
x = 10  # Gv
def  outer():
	def   inner():
		print(x)  #  Gv  i.e.  10
	# End  of  inner  function		
	inner()  #  Executes  inner()  function
# End  of  outer  function	
outer()  #  Executes  outer()  function




'''
1) When  can  inner  function  use  global  variable  ?  ---> 
															When  inner()  and  outer()  functions  do  not  have  variable  with  same  name

2) In  which  order  is  variable  searched ?  --->  Inner  function , outer  function  and  Gv
'''
