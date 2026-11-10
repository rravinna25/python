#  Find  outputs  (Home  work)
class   c1:
	def  m1(self):  #  self  is  object 'a'
		x = 10  # Lv  of  m1()  method
		self . x = 20  #  Adds variable  'x'  to  object  'a'  with  value  20
		print(x)  #  Lv  i.e.  10
		print(self . x) #  a . x  i.e. 20
		x += 5  #  Modifies  Lv  to  15
		self . x += 7  #  Modifies  a . x  to  27
    #  Lv  'x'  is   lost
	def   m2(self):
		#print(x) #  Error :  Method  m2()  does  not  variable  'x'
		print(self . x)  #   a . x  i.e.  27
		self . x += 6  #  Modifies  a . x  to  33
	# Nothing  is   lost
# End  of  the  class
a = c1() #  Creates  an  empty  c1  class  object
a . m1()  #  Executes  m1()  method  of  class  c1
a . m2()  #  Executes  m2()  method  of  class  c1
print(a . x)  #  33
#print(self . x) #  Error :  Object  self  does  not  exist
#print(x)  #  Error :  Gv  'x'  does  not  exist


'''
10
20
27
33


Local  variable  --->  x = 15 
Object  a   --->  x = 33


1) Who  can  use  self ?  ---> Just   method

2) Who  can  not  use  self ?  --->  Function  and  outside  the  class
'''
