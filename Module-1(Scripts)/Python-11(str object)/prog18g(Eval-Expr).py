'''
Write  a  program  to  evaluate  an  expression  which  contains  only  +  symbols
Let  input  be   25 + 10.8 + True
Print  the  sum  result
'''
try:
	a = input('Enter the expression: ')   #   25 + 10.8 + True
	sum = 0
	list = a . split('+'):   #   ['25' , '10.8' , 'True']  i.e. splits  on  '+'  
	for  x  in   list:   #  'x'  is  each  element  of  list
		sum += int(x)  #  Adds  each  number  to  sum
	print('Sum: ', sum)   #  Sum of  inputs
except:
	print('Invalid expression')
