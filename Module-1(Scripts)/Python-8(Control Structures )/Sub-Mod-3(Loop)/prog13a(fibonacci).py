'''
Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

Let  input  be  6
What  is  the  output ?  --->  First  6  terms  i.e.  0 , 1  , 1 ,  2 , 3 , 5
'''
n = int(input('Enter number of terms : '))  
if  n == 0:
	exit()  #  Print  nothing  when  input  is  0
print('Fibonacci series')
if  n == 1:  
	print(0)
	exit()  #  Stops  execution  when  input  is  1
a = 0  #  1st  term	
b = 1  #  2nd  term
print(a)  #  First  term  i.e.  0
print(a)  #  2nd  term  i.e.  1
c = a + b #  3rd  term  i.e.  1
for  i  in   range(n - 2):  #   Prints  remaining  (n - 2)  terms  of  the  series
	print(c)  #  Each  term  from  3rd  term
	a = b  #  Modifies  a   and  b
	b = c
	c = a + b    #  Each  term  is  sum  of  the  two  preceding  terms
