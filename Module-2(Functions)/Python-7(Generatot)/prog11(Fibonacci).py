'''
Write  a   generator  to  generate  fibonacci  series  upto  'x'

Let  'x'  be  10

What  are  the  outputs ?  --->  0 , 1 ,  1 , 2 , 3 , 5 , 8 

Hint:  Use  generator  function  and  for  loop
'''
import time
def   fib(x):
	a , b  = 0 , 1   #  1st  and  2nd  terms  of  fibonacci  series	
	while  a <= x: #  Repeat  until  a > user  input
		yield  a  #  Yields  each  term  to  for  loop  variable  'y'
		a , b  =  b , a + b  #  Modifies  values  of  a  and  b		
# End  of  generator
x = int(input('Enter the last value of fibonacci series:'))
g = fib(x)  #  Creates  an  empty  generator  object
for  y  in  g:  #  'y'  is   each  term  yielded  by  generator  function
	print(y)  #   Each  term  of  fibonacci  series
	time . sleep(0.5)
print('End')
