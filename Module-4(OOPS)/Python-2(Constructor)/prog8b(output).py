# Find  outputs (Home  work)
class    c1:  # Deleted  becoz  function  is  defined  with  same  name  later
	def   __init__(self):
		print('Constructor')
def  c1():  #  Alive :  function  is  defined  at  the  end
	print('Function')
# End  of  the  class
a = c1() #  Executes  function  c1()  which  returns  None  by  default  i.e.  a = None
print(a) # None

'''
Function
None
'''
