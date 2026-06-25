# How  to  call  f1()  function  when  @decor  tag  is  missing  ?
def   decor(fun): #  fun  is  f1
	def   inner():
		x = fun()  #   Executes  function  f1()  thru  ref  fun  which  returns  10   i.e.  x = 10
		return   x + 2 #  12  is  returned  to  function  call  f1()
	return  inner #  Returned  to  function  call  decor(f1)
def  f1():
        return  10  #  10  is  returned  to  function  call   fun()  i.e.  f1()
#end  of  the  function
f1 = decor(f1)  #  Executes  decor()  function  which   returns  inner  function  i.e.  f1 = inner  --->  f1  points  to  inner()  function
print(f1())  #  Executes  inner()  function  thru  ref  f1  i.e.  print(inner())  --->   print(12)


'''
1) What  is  the  issue  without  @decor  tag ?  --->
																	decor()  function  needs  to  be  called  explicitly  with  f1 = decor(f1)

2) What  is  the  advantage  of  @decor  tag ?  --->  decor()  function  is  automatically   executed

3) How  is  @decor  tag  internally  interpreted ?  --->   f1 = decor(f1)

4) Finally,  what  is  recommended ?  --->  @decor  tag
'''
