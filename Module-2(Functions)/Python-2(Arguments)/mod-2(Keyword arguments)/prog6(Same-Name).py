# Find  outputs  (Home  work)
def  f1(x):  # Deleted :   Another  function  is  defined  with  same  name
	print('1st  function : ' , x)
def  f1(y):   # Deleted :   Another  function  is  defined  with  same  name
	print('2nd  function : ' , y)
def  f1(z):  #  Recognized :   Last  function
	print('3rd  function : ' , z)
f1(z = 10)  # 3rd  function : 10
#f1(y = 20) #  Error :  Function  f1()  expects  argument  'z'  but  not  'y'  
#f1(x = 30) #  Error :  Function  f1()  expects  argument  'z'  but  not  'x'  


'''
Which  function  is  executed  when  multiple  functions  have  got  same  name ?  --->
																		The  last  function  is  executed  and  rest  are  deleted
'''
