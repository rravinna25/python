#  Find  outputs  (Home  work)
def   m1():
		print('Function')
class   c1:
	def   m1(self):  #  Deleted  becoz   another  method  is  defined  with  same  name
		print('1st  method')
	def   m1(self):  #  Deleted  becoz   another  method  is  defined  with  same  name
		print('2nd  method')
	def   m1(self): #  Alive  becoz  it  is  the  last  method
		print('3rd  method')
# End  of  class  c1
a = c1()   #  Creates  c1  class  object
a . m1() #   Executes  the  last  m1()  method  of  class  c1  i.e. 3rd  method
m1() #   Executes  function  m1()


'''
3rd  method
Function


Which  method  is  executed  when  methods  have  same  name ?  --->  The  last   method  and  rest  are  deleted
'''
