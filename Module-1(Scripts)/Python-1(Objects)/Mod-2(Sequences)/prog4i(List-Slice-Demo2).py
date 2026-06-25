#  Find  outputs  (Home  work)
#        0      1         2        3          4       5         6        7
list = [25 , 10.8 , 3+4j , 'Hyd' , True , None , 10.8 , 'Hyd']
x ,  y = list[3 : 5]  #  x , y = ['Hyd' , True]
print('x : ' , x)  #  x :  Hyd
print('y : ' , y) #   y : True
for  x  in  list[2:7]:  #  for   x  in  [3+4j , 'Hyd' , True , None ,  10.8]
	print(x) #  3+4j  <next line>  Hyd  <next line>  True  <next line>  None  <next line>   10.8  <next line>


'''
for  x  in  list:
	print(x)
for  x  in  list[2 : 7]:
	print(x)
What  is  the  difference  between  the  two  for  loops  ?  --->  First  for  loop  iterates  thru  whole  list  but
																									 2nd  for  loop  iterates  thru  sliced  list
'''
