#  Find  outputs  (Home  work)
class   c1:
	def  __init__(self):  #  Deleted  becoz  class  has  another  constructor
		print('No  argument  constructor')
	def  __init__(self , x):  #  Deleted  becoz  class  has  another  constructor
		print('single  argument  constructor : ' , x)
	def  __init__(self , x , y):  #  Alive :   Last  constructor
		print('Two  argument  constructor : ' , x , y)
# End  of  the  class
a = c1(10 , 20) #  Executes  the  last  constructor  of  class  c1  :  self  is  object  'a'  , x = 10 , y = 20
#b = c1(30) # Error :  Last  constructor  expects  2  args  but  single  arg  is  passed  
#c = c1()  # Error :  Last  constructor  expects  2  args  but  zero  args  are  passed 


#  Output  ---> Two  argument  constructor : <space> 10 <space> 20
