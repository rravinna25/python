# Find  outputs  (Home  work)
class   c1:  #  Deleted  becoz  another  class  is  defined  with  same  name
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:  #  Deleted  becoz  another  class  is  defined  with  same  name
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:  #  Alive  becoz   it  is  the  last  class
	pass
a = c1() #  Creates  3rd c1 class  object
#a . m1() #  Error :  3rd  c1  class  does  not  have  m1()  method
