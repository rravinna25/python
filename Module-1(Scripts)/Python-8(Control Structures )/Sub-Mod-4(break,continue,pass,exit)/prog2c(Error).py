# Identify  Error  (Home  work)
class   c4:  #   c4  is  iterable  but  not  iterator
	def  __iter__(self):
		print('__iter__  method ')
		return   self #  Error :  __itr__()  method  should  return  iterator  but  itr  is not  an  iterator
# End  of  the  class
itr = c4()  #  Empty  object
for  x  in   itr:  #   Valid  :   for  loop  can  iterate  thru  itr  as  itr  is  iterable  class  object
	print(x)


'''
What  is  the  issue  with  return  self  in   __iter__()  method ?  --->  self  (i.e.  object  itr)  is  not  an  iterator
																										       becoz  class  c4  does  not  have  __next__()  method  
'''
