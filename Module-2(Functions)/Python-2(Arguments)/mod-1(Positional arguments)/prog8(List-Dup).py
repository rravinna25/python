'''
#  Write  a  function  which  returns  True  if  list  has   duplicate  elements  and  False  if  all  the  elements  are  unique
def  has_duplicates(??):
    return  True  if  list  has   duplicate  elements  and  False  if  all  the  elements  are  unique
# End  of  the  function
How  to  read  list
print('Does  list  have  duplicate   elements  :  ' , ???)
'''
def has_duplicates(a):
	if(len(a)!=len(set(a))):
		return True
	return False	
#  End  of  the  function	
a = eval(input('Enter List : '))
print('Does list have duplicate elements :', has_duplicates(a))
