# Find  outputs(Home  work)
def   decor(fun): # fun =wish(name)
	print(fun . __name__) # wish
	def    inner(name):
		if   name  == 'Python':
			print('Hello' , name)
		else:
			fun(name)  #  Executes  function  wish()  thru  ref  fun  which  prints   Hi  Java
	return  inner # returned to function call
@decor # wish = decor(wish)  --->  Executes  decor()  function  which  returns   inner  function  i.e.  wish = inner  --->  Ref  wish  points  to  inner()  function
def    wish(name):
        print('Hi' , name)
# End  of  the  function
wish('Python')  #  Executes  inner()  function  thru  ref  wish  which  prints   Hello  Python
wish('Java')  #  Executes  inner()  function  thru  ref  wish  which  prints   Hi  Java


'''
wish
Hello Python
Hi Java


What  are  the  outputs  without  decoration ?  --->  Hi  Python
																		           Hi  Java
'''
