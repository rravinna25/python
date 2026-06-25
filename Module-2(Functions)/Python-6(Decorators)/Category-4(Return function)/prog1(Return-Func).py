# Find  outputs
def  outer():
	print('outer  function')
	def  inner():
		return  10  #  10  is   returned  to  function  call  x()
	return  inner  #  inner  function  is   returned  to  function  call  outer()
# End  of  the  function
x = outer()   #   Executes  outer()  function  which  returns  inner  function  i.e.  x = inner  ---> Ref  'x'  points  to  inner()  function
print(x()) #  Executes  inner()  function  as  'x'  points  to  inner()  function  which  returns  10  i.e.   10
#print(inner())  #   Error :  inner()  function  is  not  visible  outside  and  hence  can  not  be  called


'''
outer  function
10
'''


'''
Function  returning  another  function
--------------------------------------------
1) How  to  return  a  function ?  --->  return  functionname

2) What  does  return  inner  do ?  --->  Returns  inner  function  to  the  outer  function  call 
													          i.e. outer()

3) What  is  the  advantage  of  returning  inner  function ?  ---> It  can  be  called  indirectly  thru  a  reference
																									  i.e.  x()

4) Can  inner  function  be  called  directly  from  other  functions  and  outside ?  --->  No  becoz  it  is  not  visible

5) return  inner()
    return  inner
    What  is  the  difference ?  --->  return  inner()  returns  result  of  inner()  function  but  
														return  inner   returns   inner  function  itself
'''
