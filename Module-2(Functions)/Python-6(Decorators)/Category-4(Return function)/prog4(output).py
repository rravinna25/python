# Find  outputs  (Home  work)
def   outer(msg):
	def  inner():
		print(msg)
	return  inner #  Returned  to  function  call  outer('Hi')  (or)  outer('Hello')
# End  of  the  function
hi_fun = outer('Hi') #  Executes  outer()  function  which   returns   inner  function  i.e. hi_fun = inner  --->  hi_fun  points  to  inner()  function
hello_fun = outer('Hello')  #  Executes  outer()  function  which  returns   inner  function  i.e. hello_fun = inner  --->  hello_fun  points  to  inner()  function
hi_fun()  #  Executes inner()  function  thru   ref  hi_fun
hello_fun()  #  Executes inner()  function  thru   ref  hello_fun


'''
Hi
Hello


What  is  enclosure ?  --->  Remembers  outer  function  argument  values  and  
										   uses  those  values  when  inner  function  is  being  executed
'''
