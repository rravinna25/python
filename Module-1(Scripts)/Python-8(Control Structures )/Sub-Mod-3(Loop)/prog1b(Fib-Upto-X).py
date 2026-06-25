'''
Write  a  program  to  print  fibonacci  series  upto   x

Let  'x'  be   10
What  are  the  outputs  ?  --->  0 ,  1 ,  1  ,  2 , 3 , 5 , 8 

1) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term
    What  is  ith  term ?  --->  (i - 1)th  term +  (i - 2)  term

2) What  are  the  first  two  terms ?  --->   0  and  1  which  are  fixed

3) Hint:  Use  while  loop

4)   Iteration               c <= x       print  'c'       a               b              c = a + b           
    --------------------------------------------------------------------------------------------
	 Initial  values          -----           ----             0               1                   1
	 
	         1                      True            1               1                1                   2
	         
			 2                      True            2               1               2                   3
			 
			 3                     True             3               2               3                   5
			 
			 4                     True             5               3               5                   8
			 
			 5                     True             8               5               8                   13
			 
			 6                      False          ---               ---             ---                ---
'''     			 
x = int(input('Enter  value  of  x  :  '))
if  x == 0:
	print('Fibonacci  series')
	print(0)
else:
	a = 0
	b = 1
	print('Fibonacci  Series')
	print(a)
	print(b)
	c = a + b
	while  c <= x:
		print(c)
		a = b
		b = c
		c = a + b
