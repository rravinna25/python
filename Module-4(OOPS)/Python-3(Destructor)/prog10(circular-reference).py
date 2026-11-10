#  Most  tricky  program
# Circular  reference (Home  work)
class   c1:
	def   __init__(self , k):  #  self  is   object  x . a   and  'k'  is  object  'x'
		print('c1  class  object  is  created')
		self . b = k  #   x . a . b = x   --->  Adds  variable  'b'  to  object  x . a  which  points  to  object  'x'
		print('End  of  c1  class constructor')
	def   __del__(self):
		print('c1  class  object  is  lost')
# End of class c1
class  c2:
	def  __init__(self):  #  self  is   object  'x'
		print('c2  class  object  is  created')
		self . a = c1(self)   #   x . a = c1(x)  --->  Adds  variable  'a'  to  object  'x'  which  points  to  c1 class  object  and  executes  constructor  of  class  c1
		print('End  of  c2  class constructor')
	def  __del__(self):
		print('c2  class  object  is  lost')
#End of class c2
print('Program  begin')
x = c2()  #  Executes  constructor  of class  c2
print('program end')
#  Executes  destructor  of  classes  c2  and   c1  before  objects  are  lost


'''
Program Begin
c2  class  object  is  created
c1  class  object  is  created
End  of  c1  class constructor
End  of  c2  class constructor
Program End
c2  class  object  is  lost
c1  class  object  is  lost



1) c2  class  object  contains  c1  class  object   reference   and  vice-versa.
    This  is  known  as  circular  reference

2) What  are  the  names  of  c2  class  object ?  --->  x   and  x . a . b
     What  is  the  name  of  c1  class  object ?  --->  x . a

3) What  are  the  four  events  after  program  terminates ?  --->
	 a) Global  object  'x'  is  lost
	 b) Executes  c2  class  destructor  before  object  'x'  is  lost
	 c) c1  class  object  is  lost  as  it  doesn't  have  reference
	 d) Executes  c1  class  destructor  before  c1  class  object  is  lost
'''
