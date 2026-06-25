# Find  outputs (Home  work)
def   outer():
	print('Outer  Function')
	def  inner():
		print('Inner function')
	return   inner #  Returns  inner  function  to  the  function  call  outer()
# End  of  the  function
fun = outer()  #  Executes  outer()  function  which  returns  inner  function  i.e.  fun = inner  --->  Ref  fun  points to  inner()  function
print('Hello')
fun()  #  Executes  inner()  function  thru  ref  fun
print('Bye')
#inner() #  Error : Not  visible  outside  and  hence  can  not  be  called


'''
Outer  Function
Hello
Inner function
Bye
'''
