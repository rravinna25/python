#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):  #  Deleted  becoz  another  method  is  defined  with  same  name
		print('No  argument  method')
	def   m1(self , x):  #  Deleted  becoz  another  method  is  defined  with  same  name
		print('Single  argument  method : ' , x)
	def   m1(self , x , y): #  Alive  becoz  it  is  the  last  method
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()  #  Creates  c1  class  object
a . m1(10 , 20) #  self  is  object  'a'  , 'x'  is  10 , 'y'  is  20  i.e. Two  argument  method : <space> 10  <space> 20
#a . m1(30) # Error :  Method  expects  2  args  but  single  arg  is  passed
#a . m1() # Error :  Method  expects  2  args  but  0  args  are passed


'''
1) Does  python  have  method  overloading ?  ---> No

2) What  is  method  overloading ?  --->  Same  method  performs  multiple  tasks

3) Does  python  have  function  overloading ?  ---> No

4) What  is  function   overloading ?  --->  Same  function  performs  multiple  tasks

5) Does  python  have  operator  overloading ?  ---> Yes

6) What  is  operator  overloading ?  --->  Same  operator  performs  multiple  tasks
'''
