# Find  outputs (Home  work)
def   f1():
	x = 'John'  # Lv  of  outer()  function
	def  f2():
		nonlocal  x  #  inner  function  uses  Lv  'x'  of  outer()  function
		x =  'Hello'  #  Modifies  Lv  of  outer()  function  to  'Hello'
	# Nothing  is  lost  as  there  is  no  Lv  in  inner  function
	f2()  #  Executes  function  f2()
	return  x  #  Returns  'Hello'  to  function  call  f1()
#  End  of  f1()  function
print(f1()) #  Executes  function  f1()  which  returns  'Hello'
