# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('c1  class constructor')
		return  25
class  c2:
	def  __init__(self):
		print('c2  class  constructor')
		return  None
class  c3:
	def  __init__(self):
		print('c3  class  constructor')
# End  of  class
# a = c1() #  Error :  Can  not  created  c1  class  object  as  c1  class  constructor  returns  non-None  i.e.  25
b = c2() #  Executes  constructor  of  class  c2  which  returns  None  and  None  is  ignored  as  constructor  is  executed  automatically
print(b) #  __str__()  method  of  object  class   returns  type  and  address  of  object  'b'
print(b . __init__()) #  Constructor  of  class  c2  prints   a  msg  and  returns  None  to  constructor  call
c = c3() #  Executes  constructor  of  class  c3  which  returns  None  and  None  is  ignored  as  constructor  is  executed  automatically
print(c . __init__()) #  Constructor  of  class  c3  prints   a  msg  and  returns  None  to  constructor  call


'''
c2  class  constructor
Type  and  address  of  object  'b'
c2  class  constructor
None
c3  class  constructor
c3  class  constructor
None



1) What  can  constructor  return ?  --->  Nothing  except  None

2) Where  is  None  returned  to ?  --->  Constructor  call  when  it  is  called  explicitly  and
															    ignored  when  it  is  automatically  executed

3) How  to  deny  object  creation ?  --->  Return  any  object  other  than  None  in  the  constructor
'''
