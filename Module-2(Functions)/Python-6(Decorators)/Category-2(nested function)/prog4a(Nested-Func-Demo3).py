# Find  outputs  (Home  work)
x = 10 #  Global  variable 
def  outer():
	x = 20  #  Local  variable  of  outer()  function
	def   inner():
		x = 30  #  Local  variable  of  inner()  function
		print(x) #    Local  variable  of  inner()  function  i.e.  30
		print(globals()['x'])  #  Global  variable i.e.  10
	# Lv  of  inner  function  is  lost
	inner()
# Lv  of  outer  function  is  lost
outer()
print('Bye')


'''
30
10
Bye


Can  inner  function  use  variable  'x'  of  outer()  function ? ---> No  becoz  inner()  function  already  has  a  local  variable  'x' 
'''
