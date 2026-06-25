# Same  decorator  to  multiple  functions  with  different  signatures
def   decor(fun):
	print(fun . __name__)
	def   inner(*x):  #  'x'  is  tuple  of  actual  parameters
		print(x)   # Tuple
		fun(*x)  #   Unpacks  tuple  'x'  to  elements  which  are  passed  to  that  function  where  fun  points
		print('End  of  decoration')
	return  inner #  Returned  to  function call
@decor  #  f1 = decor(f1) ---> Executes  function  decor()  which  returns  inner  function  i.e.  f1 = inner  --->  Ref  f1  points  to  inner()  function
def   f1(x): #  x  is   10
	print('f1  function  :  ' , x)
@decor  #  f2 = decor(f2)  ---> Executes  function  decor()  which  returns  inner  function  i.e.  f2 = inner  --->  Ref  f2  points  to  inner()  function
def   f2(x , y): #  x  is  25  and  y  is  10.8
	print('f2  function  :  ' , x , y )
@decor   #  f3 = decor(f3)  ---> Executes  function  decor()  which  returns  inner  function  i.e.  f3 = inner  --->  Ref  f3  points  to  inner()  function
def  f3(x , y , z):#  x  is  'Hyd' , 'y'  is  True  and  'z'  is  3+4j
	print('f3 function : ' , x , y , z)
@decor  #  f4 = decor(f4)  ---> Executes  function  decor()  which  returns  inner  function  i.e.  f4 = inner  --->  Ref  f4  points  to  inner()  function
def   f4():
	print('f4 function')
# End  of  the  function
f1(10)  #   Executes  inner  function  thru  ref  f1  and  tuple  of  single  element  is  passed  to  inner()  function  i.e.  (10,)
f2(25 , 10.8) # Executes  inner  function  thru  ref  f2  and  tuple  of  two  elements  is  passed  to  inner()  function  i.e.  (25 , 10.8)
f3('Hyd' ,  True  , 3 + 4j) # Executes  inner  function  thru  ref  f3  and  tuple  of  three  elements  is  passed  to  inner()  function  i.e.  ('Hyd' , True , 3 + 4j)
f4()  # Executes  inner  function  thru  ref  f4  and  empty  tuple  is  passed  to  inner()  function  i.e. ()


'''
f1
f2
f3
f4
(10,)
f1  function  :   10
End  of  decoration
(25, 10.8)
f2  function  :   25 10.8
End  of  decoration
('Hyd', True, (3+4j))
f3 function :  Hyd True (3+4j)
End  of  decoration
()
f4 function
End  of  decoration



How  is  same  decorator  used  when  functions  have  different  number  of  arguments ?  --->
																														Since  inner()  function  is  var-arg  function
'''
