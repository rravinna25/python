# Find outputs  (Home  work)
class  c1:  #  Deleted  becoz  function  is  defined  with  same  name  later
        def  __init__(self):
                print('Constructor')
def  c1(x):  #  Alive
	print('Function : ' , x)
# End  of  class  c1
#a = c1() # Error :  Function  c1()  expects  an  argument  but  nothing  is   passed  
b = c1(25) #  Executes  function  c1(25)  which  returns  None  by  default  i.e.  b = None
print(b) # None


'''
Function :  25
None
'''
