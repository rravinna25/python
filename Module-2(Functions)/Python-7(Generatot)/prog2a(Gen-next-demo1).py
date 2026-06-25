# Defining  generator  through  function
import   time
def   f1():   #  It  is  generator  function  due  to  yield
	print('One')
	yield  25  #  25  is   returned  to  next(g)
	print('Two')
	yield  10.8  #   10.8  is   returned  to  next(g)
	print('Three')
	yield  'Hyd' #   'Hyd'   is   returned  to  next(g)
	print('Four')
# End  of  generator
g = f1()   #  Creates  an  empty  generator  object
print(type(g))  #  <class  'generator'>
print(g)    #  __str__()  method   returns  type  and  address of  object  'g'
print(type(f1))  #  <class  'function'>
while  True:
	try:
		print(next(g)) #  Yields  next  element  of   object  'g'
		time . sleep(1)
		print('Hello') #   Hello
	except  StopIteration:
		break
#  End  of  while  loop
print('End')
#print(len(g)) # Error : 'g'  is  not  a  sequence
#print(next(g)) #  Raises  StopIteration  Error  as  there  is  no  5th  element  in  object  'g'


'''
<class 'generator'>
Type  and  address  of  object  'g'
<class 'function'>
One
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End


1) What  does  f1()  do  if  f1  is  a  regular  function ?  ---> Executes  f1()  function

2) What  does  f1()  do  if  f1  is  a  generator  function ?  --->  Creates  an  empty  generator  object

3) When  is  generator  function  executed ?  --->  As  soon  as  next(g)  is  called  where  'g'  is   a  generator

4) What  does  1st  call  to  next(g) do ?  --->  Executes  generator  function  from  the  begining  till   first  yield  statement

5) What  does   subsequent  call  to  next(g) do ?  --->  Resumes  generator  function  from  where  it  got  paused  and
																					  continues  till   the  next  yield  statement

6) What  does  next(g)  do  when  generator  yields  nothing ?  ---> Raises  StopIteation  error
'''
