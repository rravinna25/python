'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 10
y = 25
'''
try:
	x = float(input('Enter  1st  input  : '))
	y = float(input('Enter  2nd  input  : '))
	print(F'Before  swap :  {x=}  \t  {y=}')
	x = x + y
	y = x - y
	x = x - y
	print(F'After  swap :  {x=}  \t  {y=}')
except:
	print('Input  should  be  float  (or)  integer')
