#  Find  outputs (Home  work)
def   decor(fun):#  fun  is  f1
	def   inner():
		print(F'Decorating  {fun . __name__}  function')
		fun()  # Executes  function  f1()  thru  ref  fun
		print('Decoration  is  finished')
	return  inner #  Returned  to  function  call  decor(f1)
@decor #  f1 = decor(f1)  --->  Executes  function  decor()  which  returns  inner  function  i.e.  f1 = inner  --->  Ref  f1  points to  inner()  function
def   f1():
	print('Hello')
# End  of  the  function
f1()  # Executes  inner()  function  thru  ref  f1
print('Bye')

'''
Decorating  f1  function
Hello
Decoration  is  finished
Bye
'''
