# Find outputs  (Home  work)
def   add(a , b):  # Deleted :  Another  function  is  defined  with  same  name
	print('2-argument  function')
	return a + b
def  add(a , b , c):   #  Deleted :  Another  function  is  defined  with  same  name
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):   #  Recognized :   The  last  function
	print('4-argument  function  :  ' , end = '')
	return a + b  + c + d
# End  of  the  function
print(add(10 , 20 , 30 , 40)) # 4-argument fucntion  :  10 + 20 + 30 + 40 = 100
print(add(50 , 60 , 70)) # 4-argument fucntion  :  50 + 60 + 70 + 4 = 184
print(add(80 , 90)) # 4-argument fucntion  :  80 + 90 + 3 + 4 = 177
print(add(100)) # 4-argument fucntion  :  100 + 2 + 3 + 4 = 109
print(add()) # 4-argument fucntion  :  1 + 2 + 3 + 4 = 10


'''
1) Which  function  is  executed  when  multiple  functions  have  got  same  name ?   --->
																														The  function  which  is  defined  last
																														
2) Where  does  ref  add  points  to  when  1st  function  is  defined ?  --->  1st  function  itself

3) Where  does  ref  add  points  to  when  2nd  function  is  defined ?  --->  2nd  function  itself
	 What  about  1st  function ?  --->   Deleted  as  it  does  not  have  reference

4) Where  does  ref  add  points  to  when  3rd  function  is  defined ?  --->  3rd  function  itself
	 What  about  2nd  function ?  --->   Deleted  as  it  does  not  have  reference
'''
