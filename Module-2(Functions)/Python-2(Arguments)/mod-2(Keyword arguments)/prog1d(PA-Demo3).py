# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) #  'a'  is  3 , 'b'  is  4 , 'c'  is  5  and  result : 23
print(f1(*[6 , 7 , 8])) #  'a'  is  6 , 'b'  is  7 , 'c'  is  8 and  result :  62
#print(f1([6 , 7 , 8])) #  Error :  'a'  is   [6 , 7,  8]  and  arguments  are  not  passed  for  'b'  and  'c'
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) #  'a'  is  1 , 'b'  is  3 , 'c'  is  5  and  result :  16
print(f1(**{'c' : 2 , 'b' :  4 , 'a' : 6})) #  'a'  is  6 , 'b'  is  4 , 'c'  is  2  and  result :  14
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # Error :  'a'  is   {'c' : 2 , 'b' :  4 , 'a' : 6}  and  arguments  are  not  passed  for  'b'  and  'c'
print({**{'c' : 2 , 'b' :  4 , 'a' : 6}}) # {'c' : 2 , 'b' :  4 , 'a' : 6}
#print(f1(**{'c' : 2 , 'a' : 4 , 'x' : 6})) #  Error  :  Arg  'x'  does  not  exist  for  f1()  function


'''
1) What  does  f1(*[6 , 7 , 8])  do  ?  --->  Unpacks  list  to  elements  6 , 7 , 8  which  are  passed  to  function  f1()
     What  are  values  of  parameters  a , b  and  c ?  --->  Elements  of  the  list  i.e.  6 , 7  and  8	 
																						
2) What  is   the  issue  with  f1([6 , 7 , 8])  ?  --->  Function  is  expecting  3  arguements  but  single  argument  is  passed
     What  is  the  value  of  parameter  'a'  ?  --->   [6 , 7 , 8]
     What  is  the  issue  with  parameters  'b'  and  'c' ?  --->  Arguments  are  not  passed  to  function  f1()

3) What  does  f1(*{1 : 2 , 3 : 4 , 5 : 6})  do ?  --->  Unpacks  dictionary  to  keys  1 , 3  and  5  which  are  passed  to  function  f1()
     What  are  values  of  parameters  a , b  and  c ?  --->  Keys  of  dictionary  i.e.  1 , 3  and  5 

4) What  does  f1(**{'c' : 2 , 'b' : 4 , 'a' : 6}  do ?  --->  Unpacks  dictionary  to  keyword  arguments   c = 2 , b = 4 , a = 6
																				        which  are  passed  to  function  f1()
     What  are  values  of  parameters  a , b  and  c ?  --->   Values  of  arguments  6 ,  4  and  2
																																	
5) What  is  the  issue  with  f1({'c' : 2 , 'b' :  4 , 'a' : 6}) ?  --->  Function  is  expecting  3  arguements  but  single  argument  is  passed
     What  is  the  value  of  parameter  'a'  ?  --->  {'c' : 2 , 'b' :  4 , 'a' : 6}
	 What  is  the  issue  with  parameters  'b'  and  'c' ?  --->  Arguments  are  not  passed  to  function  f1()								
'''
