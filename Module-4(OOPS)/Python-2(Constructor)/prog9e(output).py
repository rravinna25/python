#  How  to  use  both  the  classes (i.e.  c1  of  prog9a  and  c1  of  current  program)  with  import  statement
import prog9a  #  Imports  prog9a  module
class   c1:
	def  __init__(self):
		print('c1  class  of  prog9e')
a = prog9a . c1() #  Executes  constructor  of  class  c1   of  prog9a  module
b = c1()  #  Executes  constructor  of  class  c1   of  current  module


'''
c1  class  of  prog9a
c1  class  of  prog9e
'''
