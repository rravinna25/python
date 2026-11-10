'''  (Home  work)
Write  a  program  to  determine  area  and  perimeter  of  triangle  and  represent  triangle  by  an  object

1) What  is  the  area  of  triangle ?  ---> sqrt(s  (s - a)  (s - b) * (s - c))

2) What  is  the  formula  for  's' ?  ---> (a + b + c) / 2

3) What  is  the  perimeter  of  triangle ?  --->  a + b + c
'''
import  math
class  triangle:
	def  get(self):  #  self  is  object   't'
		self . a = eval(input('Enter  first  side  of  triangle : ')) # Adds  variable  'a'  to  object  self  with  user  input
		self . b = eval(input('Enter  second  side  of  triangle : ')) # Adds  variable  'b'  to  object  self  with  user  input
		self . c = eval(input('Enter  third  side  of triangle : ')) # Adds  variable  'c'  to  object  self  with  user  input
	def  test(self): #  self  is  object   't'
		 if  self . a + self . b > self . c  and  self . b + self . c > self . a  and  self . c + self . a > self . b:   #  Sum  of  every  2  sides  should  be  >  3rd  input
				pass  #  Do  nothing
		 else:
				print('Not  a  triangle')
				exit()  #  Stops  execution
	def  area(self):  #  self  is  object   't'
			s = (self . a + self . b + self . c) / 2
			return   math . sqrt(s * (s - self . a) * (s - self . b) * (s - self . c))  #  Area  of  triangle
	def  peri(self):  #  self  is  object   't'
			return  self . a + self . b + self . c  #  Perimeter  of  triangle
# End of the class
if  __name__  ==  '__main__':
	t = triangle() #  Creates  an  empty  triangle  class  object
	t . get()  #  Reads  inputs  to  object  't'
	t . test() #  Are  values  of  object  't'  valid ?
	print('Area : ',  t . area())   #  Area  of  values  in  object  't'
	print('Perimeter : ', t . peri())  #  Perimeter  of  values  in  object  't'



# Object  't'  ---> a  =  3  ,  b = 4 ,  c  = 5


'''
1) What  are  a , b , c  called ?  --->  Instance  variables  of  object  't'

2) What  is  's'  called ?  ---> Local  variable  of  area()  method

3) t . s = (self . a + self . b + self . c) / 2
    What  is  the  issue ?  --->  Adds  variable  's'  to  object  't'  but  triangle  class  object  should  have  three  variables  
											   but  not  four

4) t = triangle()
    How  many  variables  are  in  object  't' ?  ---> Nothing  becoz  every  object  is  initially  empty

5) t . get()
    How  many  variables  are  in  object  't' ?  --->  
													Three  Variables  a , b  and  c  becoz  get()  method  adds  three  variables  to  object  't'
													
6) Can  methods  of  traingle  class  use  object  't'  even  though   argument  name  is  self ?  --->
																																	Yes  becoz  't'  is  global  object													
'''
