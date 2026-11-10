# Find  outputs  (Home  work)
class   c1:  #  Deleted  becoz  another  class  is  defined  with  same  name
	def   m1(self):
		print('Method  of  first  c1  class')
class   c1:  #  Deleted  becoz  another  class  is  defined  with  same  name
	def   m1(self):
		print('Method  of  second  c1  class')
class   c1:  #  Alive  becoz   it  is  the  last  class
	def   m1(self):
		print('Method  of  third  c1  class')
a = c1() # 3rd  c1  class  object
a . m1() #  Executes  method  of  3rd  c1  class  i.e.  Method  of  third  c1  class


'''
1) Which  class  is  alive  when  multiple  classes  have  same  name ?  --->  The  last  class  and  rest  are  deleted

2) Can  two  classes  have  same  name  in  c++  and  java ?  --->  No
'''
