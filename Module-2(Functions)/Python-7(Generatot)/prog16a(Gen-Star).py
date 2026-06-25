# How  to  unpack  generator  object   with  *  operator ?
def   f1():  #  It  is  generator  function  due  to  yield
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End of  generator
g = f1() #  Creates  an  empty  generator  object
print('Begin')
print(*g)    #  4  events
print('End')


'''
Begin
One
Two
Three
Four
25  <space> 10.8  <space>  Hyd
End
'''


'''
1) What  are  the  four  events  in  execution  of  *g  ?  --->
	a) Executes  the  whole  generator  function  without  stopping  in  the  middle  even  though  there  is  yield  statement
	b) All  the  elements  which  are  yielded  by  generator  function  are  stored  in  generator   object  'g'
	c) Unpacks  generator  object  to  elements (due  to  *  operator) i.e.  25 , 10.8 , Hyd
	d) Generator  becomes  empty  after  unpack

2) Do  we  need  to  handle  StopIteration  error ?  --->   No  and  it  is  internally  handled  by  *  operator

3) What  are  the  two  drawbacks  of  *g ?   --->  a) Waiting  time  when  there  are  too  many  yield  statements
																			  b)  Possibility  of  MemoryError

4) Hence  *g  is  not  recommened  for  generator  when  there  are  too  many  elements

5) Therefore  for  loop  (or)  next(g)  is  recommended  for  generator
'''
