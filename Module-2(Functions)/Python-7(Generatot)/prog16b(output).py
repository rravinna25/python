#  Find  outputs
def   f1():
	x = 1
	while  x <=  100000000000000000000:
		yield  x #   Yielded  to  object  'g'
		x +=  1
# End of  generator
g = f1()  #  Creates  an  empty  generator  object
print('Begin')  # Begin
print(*g)   #  Waiting  time  (or)  memory  error  due to   too  many  elements  in   generator
print('End') #  Skipped 


'''
1) What  are  the  two  drawbacks  of  *g ?   --->  a) Waiting  time  due  to  too  many  elements
																			  b)  Possibility  of  MemoryError  when  there  is  no  sufficient  memory

2) Hence  *g  is  not  recommened  for  generator  when  there  are  too  many  elements

3) Therefore  for  loop  (or)  next(g)  is  recommnded  for  generator
'''
