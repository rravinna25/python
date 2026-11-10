#  Find  outputs (Home  work)
from  prog9a  import  c1  #  Deletes  class  c1  which  is  imported  becoz  another  class  c1  is  defined  with  same  name  later
class   c1:  #  Alive
	def  __init__(self):
		print('c1  class  of  prog9b')
a = c1() #  Executes  constructor  of  class  c1  in  same  module  i.e. prog9b


'''
Why  is  c1  class  of  prog9a  deleted ?  --->  Since  another  class  with  same  name  c1  is  defined  later  in  the  current  module
'''
