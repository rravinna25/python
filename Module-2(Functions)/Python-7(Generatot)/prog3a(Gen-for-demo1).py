# How  to  iterate  generator  with  for  loop
import  time
def   f1(): #  It  is  generator  function  due  to  yield
	print('One')
	yield  25  #   25  is   returned  to  for  loop  variable  'x'
	print('Two')
	yield  10.8  #    10.8  is   returned  to  for  loop  variable  'x'
	print('Three')
	yield  'Hyd'   #   'Hyd'   is   returned  to  for  loop  variable  'x'
	print('Four')
# End  of  generator
g = f1()  #  Creates  an  empty  generator  object
for  x  in  g:  #  'x'  is  that  element  yielded  by  generator
	print(x)
	time . sleep(1)
	print('Hello')
#  End  of  for  loop
print('End')
print(g)   #  __str__()  method   returns  type  and  address  of  object  'g'
#print(next(g)) #  StopIteration  as  there  is  no  5th  element  in  generator
g = f1() # Creates  another  generator  object  i.e.  2nd  object
print(next(g))  #  Prints  'One'  and  yields  25


'''
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
Type  and  address  of  object  'g'
One
25


1) What  are  the  two  ways  to  iterate  a  generator ?  --->  next(g)  in  while  loop
																								     and
																								 for   x  in   g:

2) list = [25 , 10.8 , 'Hyd']
    Is  next(list) valid ?  --->  No  becoz  next()  function  expects  iterator  (i.e. generator)  but   sequence(i.e.  list)  is  passed

3) How  to  iterate  a  sequence ?  --->  With  for  loop  only  
														       i.e.  for  x  in  sequence:

4) What  is  recommened  to  iterate  a  generator(for  loop  (or)  next()  function)  and   why  ?  --->																																								
																		for  loop   becoz  StopIteration  error  is  internally  handled  by  for  loop

5) How  long  is  for  loop  executed ?  --->  Until  StopIteration  error  is  raised
'''
