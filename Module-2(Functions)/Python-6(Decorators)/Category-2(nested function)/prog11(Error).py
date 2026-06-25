#  Identify  Error
x = 10  #  Global  variable
def   outer():
	x = 20  #  Lv  of   outer()  function
	def  inner():
		global   x  #  Treats  'x'  as  GV
		nonlocal  x  #  Error  :  'x'  is  already  global  and  hence  can  not  use  Lv  of  outer()  function


'''
Inner  function  can  use  either  nonlocal  keyword  (or)  global  keyword  but  not  both  simultaneously
'''
