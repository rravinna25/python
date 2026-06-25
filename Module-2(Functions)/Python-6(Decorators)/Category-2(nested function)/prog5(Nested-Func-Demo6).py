# Find  outputs  (Home  work)
def  outer():
	x = 10  #  Local  variable  of  outer()  function
	def  inner():
		x = 20  #  Local  variable  of  inner()  function
		print(x) #  Local  variable  of  inner()  function  i.e.  20
		x +=  7  #  Modifies  local  variable  of  inner()  function  to  27
	# Local  variable  of  inner  function  is  lost
	print(x)  #  Local  variable  of  outer()  function  i.e.  10
	x += 5  #  Modifies  local  variable  of  outer()  function  to  15
	inner()  #  Executes   inner()  function
	print(x)  #  Local  variable  of  outer()  function  i.e.  15
# Local  variable  of  outer  function  is  lost
outer()  #  Executes  outer()  function
print('Bye')


'''
10
20
15
Bye
'''
