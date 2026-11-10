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
        return   a  #  Returns  object  'a'  to  function  call  f1()
#  Executes  destructor  before  local  object  'a'  is  lost
print('Program  Begin')
f1()  #  Executes  function  f1()  which  returns  object  'a'  which  is  ignored
print('Program  End')


'''
Program Begin
Function Begin
Object  is    created
Function End
Object is Lost
Program End


Why  is  object  'a'   lost  after  f1()  function  terminates ?  --->  Since  it  doesn't  have  reference  
'''
