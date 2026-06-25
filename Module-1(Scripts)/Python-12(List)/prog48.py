'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]

       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                           0      1       2       3
								
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint :  Unsorted  lists  can  not  be  merged
'''
try:
	a = eval(input('Enter  1st  list  : '))
	b = eval(input('Enter  2nd  list  : '))
	a  . sort()
	b  . sort()
	c = []
	i = j = 0
	while  True:
		if  a[i] < b[j]:
			c . append(a[i])
			i += 1
		else:
			c . append(b[j])
			j += 1 
except:			
	print(c + a[i:] + b[j:])
