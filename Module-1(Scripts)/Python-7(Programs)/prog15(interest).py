'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest

2) What  are  the  outputs ? ---> Simple  interest   and   compound  interest

3) What  is  simple  interest  formula ?  --->  ptr / 100

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
'''
try:
	p = float(input('Enter  principle  :  '))
	t = float(input('Enter  time  : '))
	r = float(input('Enter  rate  of  interest :  '))
	si = p * t * r / 100
	ci = p * (1  +  r  /  100) **  t  -  p
	print(F'Simple  Interest : {si:.2f}')
	print(F'Compound  Interest : {ci:.2f}')
except:
	print('Input  should  float  (or)  integer')
