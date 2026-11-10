# Find  outputs  (Home  work)
class   c2:
	def  __init__(self):
		print('outer  class  constructor')
	class   c2:
		def __init__(self):
			print('inner  class  constructor')
#end of the class
a = c2() # Executes  constructor  of  outer  class  c2
b = a . c2() # Executes  constructor  of  inner  class  c2
c = c2 . c2() # Executes  constructor  of  inner  class  c2
d = c2() . c2()  #  Executes  constructors  of  outer  class  and  inner  class


'''
outer  class  constructor
inner  class  constructor
inner  class  constructor
outer  class  constructor
inner  class  constructor
'''
