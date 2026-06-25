'''
Write  a  program  to  concatenate  two  strings  separated  by  space  but  swap  first  two
characters  of  the  two  strings.
Assume  that  each  string  has  a   minimum  of  two  characters

Let  inputs  be  Java  and  Python
What  are  the  outputs ?  --->  Pyva<space>Jathon

Hint:  Use  slice
'''
a = input('Enter first string: ') 
b = input('Enter second string: ') 
if len(a) < 2 or len(b) < 2:
	print('Input  should  be  a  min  of  2-char  string')
else:
	print('Result  :  ' ,  b[: 2] + a[2 :] + ' ' + a[: 2] + b[2 :])


'''
1) What  does  b[:2]  do ?  --->  Extracts  first  two  characters  of  2nd  string

2) What  does  a[2:]  do ?  --->  Extracts  first  string   without  first  two  characters  

3) What  does  a[:2]  do ?  --->  Extracts  first  two  characters  of  1st  string

4) What  does  b[2:]  do ?  --->   Extracts  2nd  string   without  first  two  characters  
'''
