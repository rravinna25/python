'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  ---> radius

2) What  is  the  output ?  --->  volume

3) What  is  the  volume  of  sphere  ?  ---> 4 / 3  * pi *  r ^ 3
'''
import  math
try:
	r = float(input('Enter  radius  :  '))
	v = 4 / 3 * math . pi * r ** 3
	print(F'Volume  :  {v:.2f}')
except:
	print('Input  should  be  float  (or)  integer')
