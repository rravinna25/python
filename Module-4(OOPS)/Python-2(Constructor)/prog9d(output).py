#  How  to  use  both  the  classes  (i.e.  c1  of  prog9a  and  c1  of  current  program)
from  prog9a  import  c1  as  c2  #  Imports  class  c1  of  prog9a  with  another  name  c2  i.e.  member  alias
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9d')
a = c1() #  Executes  constructor  of  class  c1  of  current  module
b = c2() #  Executes  constructor  of  class  c1  imported  from  prog9a


'''
c1  class  of  prog9d
c1  class  of  prog9a


We  are  able  to  use  both  the  c1  classes  of  prog9a  and  prog9d  and  this  is  possible  with  member  alias
'''
