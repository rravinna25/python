# Find  outputs  (Home  work)
class   outer:
	def  __init__(self):
		print('Outer  class  object   is  created')
	def  m1(self):
		print('Outer  class  method')
	class   inner:
		def __init__(self):
			print('Inner  class  object   is  created')
		def m1(self):
			print('Inner  class  method')
#end of the class
o = outer() # Executes  outer  class  constuctor
o . m1() #  Executes  method  of  outer  class  as  'o'  is  outer  class  object
i1 = o . inner()  #  Creates  inner  class  object  wrt  outer  class   object  and  executes   inner  class  constuctor
i1 . m1()  #  Executes  method  of  inner  class  as   i1  is  inner  class  object
i2 = outer . inner()  #  Creates  inner  class  object  thru  outer  class   name  and  executes   inner  class  constuctor
i2 . m1() # Executes  method  of  inner  class  as   i2  is  inner  class  object
i3 = outer() . inner()  #  Creates  outer  and  inner  class  objects  and  executes  outer  and  inner  class  constuctors
i3 .m1()  #  Executes  method  of  inner  class  as   i3  is  inner  class  object
#i = inner()  #  Error : Can  not  inner  class  object  directly  without  outer  class  object  (or)  outer  class  name


'''
Outer  class  object   is  created
Outer  class  method
Inner  class  object   is  created
Inner  class  method
Inner  class  object   is  created
Inner  class  method
Outer  class  object   is  created
Inner  class  object   is  created
Inner  class  method


1) What  are  the  members  of  outer  class ?  --->  Constructor , m1()  method  and  inner  class

2) What  are  the  members  of  inner  class ?  --->  Constructor  and   m1()  method
'''
