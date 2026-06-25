#  Find  outputs
#f2()  #  Error  :  Function  f2()  is  defined  later
def  f1():
		print('f1  Function')
		f2()  #  Valid :  function  can  be  called  before  it  is  defined  
		print('Back  to  f1  function')
def  f2():
		print('f2  function')
f1()  #  Executes  function  f1()
print('Bye')



'''
Can  a  function  be  called  before  it  is  defined ?  --->  Yes  when  a  function  calls  another  function
																											and
																					      No  when  a  function  is  called  from  outside																											
'''
