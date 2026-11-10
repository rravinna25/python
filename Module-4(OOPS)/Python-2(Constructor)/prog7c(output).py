#  Find  outputs
class   c1:
	def  __init__(self):  #  Deleted  becoz  class  has  another  constructor
		print('No  argument  constructor')
	def  __init__(self , x):  #  Deleted  becoz  class  has  another  constructor
		print('single  argument  constructor : ' , x)
	def  __init__(self , x = 100 , y = 200):  #  Alive :   Last  constructor
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20)  #  Executes  the  last  constructor  of  class  c1  :  self  is  object  'a'  , x = 10 , y = 20
b = c1(30) #  Executes  the  last  constructor  of  class  c1  :  self  is  object  'b'  , x = 30 , y =  default  value  200
c = c1()  #  Executes  the  last  constructor  of  class  c1  :  self  is  object  'c'  , x =  default  value  100 , y =  default  value  200


'''
Two  argument  constructor : <space> 10 <space> 20
Two  argument  constructor : <space> 30 <space> 200
Two  argument  constructor : <space> 100 <space> 200
'''
