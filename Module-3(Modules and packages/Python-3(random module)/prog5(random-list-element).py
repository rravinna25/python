# Write  a  program  to  print  random  element  of  the  list  ten  times   (Home  work)
import random
try:
	list = eval(input('Enter a List : '))  #  Reads  a  list
	for  x  in  range(10):   #  10  random  elements
		print(random . choice(list))   #   Random  element  of  the  list
except  IndexError:
	print('Input  can  not  be  empty  list')


'''
What  does  choice([])  do ?  --->   Raises  IndexError  becoz  choice()  function  internally  uses  indexes  but
										              empty  list  does  not  have  indexes
'''
