#  Decoartor  chaining  demo  program
def   decor2(fun):  #   fun   is   inner1()  function
	print(fun . __name__)  #    inner1  becoz  fun  points  to   inner1()  function
	def  inner2(name): #  name  is   'Hyd'
		print('Decorator2  execution')
		fun(name)  #   Executes  inner1()  function  thru  ref  fun  i.e.  inner1('Hyd')
		print('Decorator2  is  finished')
	return  inner2   #  Returned  to   function  call  decor2(inner1)
def  decor1(fun):  #  fun  is  wish()  function
	print(fun . __name__) #   wish  becoz  fun  points  to  wish()  function
	def   inner1(name):  # name  is   'Hyd'
		print('Decorator1  execution')
		fun(name)  #  Executes  wish()  function  thru  ref  fun  i.e.  wish('Hyd')
		print('Decorator1  is  finished')
	return  inner1  #  Returned  to  function  call  decor1(wish)
# End  of  the  function
@decor2  #  wish = decor2(decor1(wish))  --->  wish = decor2(inner1)  --->  wish =  inner2  --->  Ref  wish  points  to  inner2()  function
@decor1
def  wish(name): #  name  is  'Hyd'
	print('Hello'  ,  name)
# End  of  the  function
wish('Hyd') #   Executes  inner2()  function  thru  ref  wish  i.e. inner2('Hyd')
print('Bye')


'''
wish
inner1
Decorator2  execution
Decorator1  execution
Hello Hyd
Decorator1  is  finished
Decorator2  is  finished
Bye
'''
