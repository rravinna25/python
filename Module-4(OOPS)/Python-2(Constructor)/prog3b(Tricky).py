# Find  outputs (Home  work)
class  c1:
	def  __init__(self):
		print('Constructor')
		b = c1()  #  Executes  constructor  of  same  class  c1  which  leads  to  recursion
# End  of  class
a = c1() #  Executes  constructor  of  class  c1


'''
1) What  is  the  morale  of  the  program?  --->  Do  not  create  object  in  the  constructor

2) What  happens  when  constructor  creates  object ? --->  Infinite  recursion

3) Where  can  object  be  created ?  --->  Any  where  in  the  program  but  not  in  the  constructor
'''
