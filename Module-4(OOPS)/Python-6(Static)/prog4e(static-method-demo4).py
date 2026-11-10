#  Find  outputs
class   c1:
	def   m1():
		print('Hyd')
#  End  of  the   class
c1 . m1()  #  Executes  static  method  m1()  of  class  c1  which  prints  Hyd
a = c1()
#a . m1() #  Error :  Treats  m1()  as  an  instance  method  becoz  it  is  called  wrt  object  and  arg  self  is  missing  for  method  m1()


'''
1) Is  m1()  a  static  method  (or)  instance  method  ?   --->  static  method  if  it  is  called  thru  classname  and
								                                                                instance  method  if  it  is  called  wrt  object
																								
2) What  is  the  issue  with  a . m1() ?  --->  Treats  m1()  as  an  instance  method  becoz  it  is  called  wrt  object  
																							and  
																	  arg  self  is  missing  for  method  m1()
'''
