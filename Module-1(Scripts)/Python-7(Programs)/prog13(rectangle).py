'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  --->  length  and   breadth

2) What  are  the  outputs  ?  --->  area  and  perimeter

3) What  is  the  area  of  rectangle  ?  ---> length * breadth

4) What  is  the  perimeter  of  rectangle ?  ---> 2 * (length + breadth)
'''
try:
	l = float(input('Enter  length  of  rectangle  : '))
	b = float(input('Enter  breadth  of  rectangle :  '))
	area = l * b
	peri = 2 * (l + b)
	print(F'Area  :  {area:.2f}')
	print(F'Perimeter :  {peri:.2f}')
except:
	print('Input  should  be  float  (or)  integer')
