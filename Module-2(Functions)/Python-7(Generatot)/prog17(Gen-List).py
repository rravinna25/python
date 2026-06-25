# Find  outputs  (Home  work)
def  f1(begin , end):
	while  begin  <=  end:
			print('Hello')
			yield  begin
			begin += 1
	print('End  of  generator')
#end of the genrator  function
g = f1(10 , 20) #  Creates  an  empty  generator  object
print('Before')
print(list(g)) #   4  events
print('After')
print(next(g))  #  Error :  Object  'g'  is  fullly  iterated  by  list(g)


'''
Before
11  times  Hello
End  of  genetator
[10 , 11 , 12 , .... 20]
After


1) What  are  the  four  events  for  list(g) ?  --->	
	a) Executes  generator  function  without  stoping  in  the  middle  even  though  there  is  yield  statement
	b) All  those  elements  which  are  yielded  by  generator  are  stored  in  generator  object
	c) Converts  generator  object  to  list
	d) generator  object  becomes  empty

2) g = f1(10 , 200000000000000) 
    What  are  the  two  drawbacks  of  list(g) ?  --->  a) Waiting  time  when  there  are  too  many  yield  statements
																				   b)  Possibility  of  MemoryError

3) Hence  list(g)  is  not  recommened  for  generator  when  there  are  too  many  elements
'''
