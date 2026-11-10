# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Object  is    created')
	def  __del__(self):
		print('Object  is  lost')
#End  of  the  class
def    f1():
        print('Function  begin')
        a  =  c1()  #  Executes  constructor
        print('Function  end')
# Executes  destructor  before  local  object  'a'  is  lost
print('Program  Begin')
b = f1()   #  Executes  function  f1()  which  returns  None  by  default  i.e.  b = None
print(b)   #  None
print('Program  End')


'''
Program Begin
Function Begin
Object is created
Function End
Object  is  lost
None
Program End


Why  is  object  'a'   lost  after  f1()  function  terminates ?  --->  Since  it   doesn't  have  reference 
'''
