#  Tricky  program
# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
	print('Function  Begin')
	a  =  c1()  #  Executes  constructor
	print(a)  #  __str__()  method  of   object  class  returns  type  and  address  of object  'a'
	print('Function  end')
	return   a  #  Returns  object  'a'  to  function  call   f1()
# Object  'a'  is   not  due  to  ref  'b'
print('Program  Begin')
b = f1() #  Executes  function  f1()  which  returns  object  'a'  i.e.  b = a  --->  Ref  'b'  points to  object  'a'  
print(b)   #  __str__()  method  of   object  class  returns  type  and  address  of object  'a'
print('Program  End')
# Executes  destructor  before  object  'b'  is  lost



'''
Program Begin
Function Begin
Object is created
Type  and  address  of  object  'a'
Function End
Type  and  address  of  object  'a'
Program End
Object is Lost


1) Why  is  object  'a'  not  lost  after  f1()  function  terminates ?  --->  
																						Since  it  has  reference  'b'  after  execution  of  b = f1()
																							
2) When  is  object   'a'  lost ?  --->  As  soon  as  program  terminates
'''
