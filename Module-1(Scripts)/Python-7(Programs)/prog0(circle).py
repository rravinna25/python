'''
Write  a  program  to  determine  area  and  circumference  of  circle

1) What  is  the  input ?  ---> Radius

2) What  are  the  outputs ? ---> Area  and  circumference

3) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2

4) What  is  the  circumference  of  circle ?  ---> 2 * 3.14159 * r
'''
import  math
try:
	r = float(input('Enter  radius  of  circle :  '))  #   Reads radius  to  object  'r'
	area = math . pi * r ** 2
	cir = 2 * math . pi * r
	print(F'Area :  {area:.2f}')
	print(F'Circumference :  {cir:.2f}')
except:
	print('Input  should  be  float  (or)  integer')



'''
What  are  the  three  events  in  every  program ?  ---> 1) Reads  inputs
																			             2) Performs  computations  on  inputs  and  derive  the  results
																						 3) Prints  results
'''
