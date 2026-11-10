#  Find  outputs  (Home  work)
class   c1:
	def   m1(self):  #  Deleted  becoz  another  method  is  defined  with  same  name
		print('No  argument  method')
	def   m1(self , x):  #  Deleted  becoz  another  method  is  defined  with  same  name
		print('Single  argument  method : ' , x)
	def   m1(self , x = 1  , y = 2):   #  Alive  becoz  it  is  the  last  method
		print('Two  argument  method : ' , x , y)
# End  of  class  c1
a = c1()  #  Creates  c1  class  object
a . m1(10 , 20) #  self  is  object  'a'  ,  'x'  is  10  , 'y'  is  20  
a . m1(30) #  self  is  object  'a'  ,  'x'  is  30  , 'y'  is   default  value  20  
a . m1() #  self  is  object  'a'  ,  'x'  is  default  value  1 , 'y'  is  default  value  2  


'''
Two  argument  method :  <space> 10 <space> 20
Two  argument  method :  <space>  30  <space>  2
Two  argument  method : <space> 1 <space> 2
'''
