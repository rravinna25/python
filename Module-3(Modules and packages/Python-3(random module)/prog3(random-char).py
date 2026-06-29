# Write  a  program  to  print  random  character  of  the  string  10  times (Home  work)
import random
try:
	str = input('Enter any string : ')  #  Reads   a  string
	for  x  in  range(10):  #  10   random  characters
		print(random . choice(str))  #  Any  random  char  of  the  string
except:
	print('Input  can  not  be  empty  string')


'''
What  does  choice('')  do ?  --->  Raises  IndexError  becoz  empty  string  does  not  have  indexes
'''
