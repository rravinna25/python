# Find  outputs  (Home  work)
class   c1:
	def   m1(self):
		print(id(self))
# End  of  the  class
a = c1()  # Creates  1st  c1  class  object
print(id(a)) #  Address  of  object  'a'
a . m1()  #  self  is  object  'a'  and  method  prints  address  of  object  'a'
b = c1()   # Creates  2nd  c1  class  object
print(id(b))  #  Address  of  object  'b'
b . m1()  #  self  is  object  'b'  and  method  prints  address  of  object  'b'
c = c1()   # Creates  3rd  c1  class  object
print(id(c))  #  Address  of  object  'c'
c . m1()  #  self  is  object  'c'  and  method  prints  address  of  object  'c'
