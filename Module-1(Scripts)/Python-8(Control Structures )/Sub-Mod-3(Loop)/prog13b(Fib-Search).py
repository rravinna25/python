'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? ---> Found

3) Do  not  print  fibonacci  series

4)                                      x  = 10

        Iteration            a              b              c          c <= x     c  ==  x
     ---------------------------------------------------------------------------
	    Initial  values      0              1              1           True        False
	    
		      1                    1              1              2           True        False
		      
			  2                    1              2             3           True        False
			  
			  3                    2              3             5           True        False
			  
			  4                    3              5             8           True        False
			  
			  5                    5              8             13           False       ----
        ------------------------------------------------------------------------
		Not  Found
			  
5)                                      x  = 21

        Iteration            a              b              c          c <= x     c  ==  x
     ---------------------------------------------------------------------------
	    Initial  values      0              1              1           True        False
	    
		      1                    1              1              2           True        False
		      
			  2                    1              2             3           True        False
			  
			  3                    2              3             5           True        False
			  
			  4                    3              5             8           True        False
			  
			  5                    5              8             13          True       False
			  
			  6                    8             13             21          True       True  --->  Found  and  do  no  search  any  more
'''
x = int(input('Enter  value  to  be  searched :  '))  
if  x == 0:
	print('Found')
	exit()  #  Stops  execution
a = 0  #  First  term
b = 1  #  2nd  term
c = a + b  #  Third  term  is  sum  of  the  two  terms  
while  c <= x:   #  Search  for  'x'  until  c > x
	if  c == x:   #  Compares  'x'  with  each  term  of  the  series
		print('Found')
		exit()  #  Stops  execution
	a = b  #  Modifies  values  of  a , b  and  c
	b = c  
	c = a + b  
#  End  of  while  loop
print('Not  Found')
