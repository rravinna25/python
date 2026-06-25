# Find  outputs(Home  work)
def   decor(fun):#  fun  is  div
	def  inner(x , y):
		try:
			return  fun(x , y)  #   Executes  function  div()  thru  ref  fun  which  returns   3.33
		except:
			return   'Division   by  0  is  not  permitted'  #  Returned  to  function  call   inner(10 , 0)
	return  inner  # Returned  to  function  call  decor(div)
@decor  #  div = decor(div)   --->  Executes function  decor()  which  returns  inner  function  i.e.   div  = inner  --->  Ref  div  points to  inner()  function
def  div(a , b):
        return  a / b  # Returned  to  function  call  fun(x , y)
# End  of  the  function
print(div(10 , 3)) #  Executes  inner()  function  thru  ref div  which  returns   3.33
print(div(10 , 0))  #  Executes  inner()  function  thru  ref div  which  returns   'Division   by  0  is  not  permitted'
#print(inner(10 , 3)) # Error : inner()  function  is  not  visible  outside  and  hence  can  not  be  called



'''
1) What  is  the  result  of  div(10 , 0)  without  decoration ?  --->  10 / 0  Throws  ZeroDivisionError

2) What  is  the  advantage  of  decoration ?  --->  div(10 , 0)  returns   a  message  but  does  not  raise  error

3) What  are  the  results  when  fun(x , y)  is  modified  to  fun(y , x) ?
     a)  div(10 , 3)  --->  3 / 10  =  0.3
     b) div(10 , 0)  --->  0 / 10 = 0.0
'''
