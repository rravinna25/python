''''
Write  three  functions:
a) first_element() :  Returns  first  element  of  the  list  and  None  if  list  is  empty
 
b) last_element() :  Returns  last  element  of  the  list  and  None  if  list  is  empty
 
c) middle_list() :  Returns  list  of  all  elements  except  first  and  last  elements,  
						    return  None  if  list  is  empty   and  
							return  empty  list  if  list  has  two  elements
'''
def first_element(list):    
	try:
		return list[0] 
	except:
		return  None
def last_element(list):
	try:
		return list[-1]  
	except:
		return  None
def middle_list(list):    	
	if  list == []:
		return  None
	return list[1:-1]  
a = eval(input('Enter List : '))
print('First element :', first_element(a))
print('Last element :', last_element(a))
print('Middle list :', middle_list(a))
