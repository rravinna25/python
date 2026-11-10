#  Find  outputs  (Home  work)
class  date:
	def   disp(self):
		print('dd : ' , self . dd)
		print('mm : ' , self . mm)
		print('yy : ' , self . yy)
	def  __str__(self):
		return  F'{self . dd} - {self . mm} - {self . yy}'
#end of the class
a =  date() # Creates  an  empty  date  class  object
a . dd = 15 # Adds  variable  dd  to  object  'a'  with  value  15
a . mm = 8  # Adds  variable  mm  to  object  'a'  with  value  8
a . yy = 1947  # Adds  variable  yy  to  object  'a'  with  value  1947
a . disp()  #  Executes  method  of  date  class  becoz  'a'  is  date  class  object
print(a) #  __str__()  method  of  date  class  returns  '15 - 8 - 1947'
print(a . __str__())  #  __str__()  method  of  date  class  returns  '15-8-1947'
print(a . __dict__) # Converts  object 'a'  to  dictionary

'''
dd : 15
mm : 8
yy : 1947
15 - 8 - 1947
15 - 8 - 1947
{'dd' : 15 , 'mm' : 8 , 'yy' : 1947}


# Object  'a'  --->   dd = 15 , mm = 8 , yy = 1947


1) How  to  print  object  in  dictionary  form ?  --->  print(object . __dict__)

2)	How  to  print  object  in   string  form ?  --->  print(object)
																				  (or)
																			 print(object . __str__())

3) How  to  print  object  in  object  form ?  --->  object . disp()
'''
