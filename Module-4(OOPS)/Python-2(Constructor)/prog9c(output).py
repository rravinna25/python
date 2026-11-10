#  Find  outputs (Home  work)
class   c1:  #  Deleted  becoz  another  class  with  same  name  is  imported  from  prog9a  later
	def  __init__(self):
		print('c1  class  of  prog9c')
from  prog9a  import  c1  #  Alive 
a = c1() #  Executes  constructor  of  class  c1  imported  from  prog9a


'''
1) Why  is  c1  class  of  current  module  deleted ?  --->  
																		Since  another  class  with  same  name  c1  is  imported  from  prog9a  later

2) In  general,  last  class  is  alive  and  rest  are  deleted
'''
