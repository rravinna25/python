# Find  outputs  (Home  work)
import  sys
class  Test:
	def  __init__(self):
		print('Constructor  :  ' , id(self))
		return    None
	def  __del__(self):
		print('Destructor  :  ' , id(self))
		return  25
# End  of  the  class
t = Test() #  Executes  constructor  which  returns  None  and  None  gets  ignored  due  to  implicit  call
print(t . __init__())  #  Executes constructor  which  returns  None  and  None  is  printed  
print(sys . getrefcount(t))  #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print(t . __del__())  #  Executes  destructor  which  returns  25  and  25  is  printed
print(sys . getrefcount(t))   #  Number  of  references  to  object  't'  i.e. 1 + 1   = 2
print('Bye')
# Executes  destructor  before  object  't'  is  lost  which  returns  25  and  25  is  ignored  due  to  implicit  call

'''
Constructor : address of  object  't'
Constructor : address of  object  't'
None
2
Destructor : address of  object  't'
25
2
Bye
Destructor : address of  object  't'


Is  object  lost  after  execution  of  destructor  ?  --->  Yes  when  it  is  automatically  executed
																													and
																						  No  when  it  is  called  explicitly    																					     
'''
