#  Find  outputs
def  f1():
	print('f1  function')
	f2()   #  Executes  function  f1()
	print('End  of  f1  function')
def  f2():
	print('f2  function')
	f1()   #  Executes  function  f1()
	print('End  of  f2  function')
f1()  #  Executes  function  f1()



'''
f1  function
f2  function
f1  function
f2  function
f1  function
f2  function
and  so  on


1) What  is  mutual  recursion ?  --->  A  function  calls  different  function  and  vice-versa

2) What  is  self  recursion ?  --->  A  function  calls  itself
'''
