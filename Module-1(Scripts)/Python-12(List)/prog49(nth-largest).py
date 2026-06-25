'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10 , 20 , 30 , 25 , 40 , 35 , 12 , 5]
Input2 :  3  (3rd  largest)
Output :   30
'''
try:
	list = eval(input('Enter list:'))  #   Reads  a  list
	while  True:		
		s = set(list)  #  Convets  list  to  set  to  avoid  duplicates
		n = eval(input('Enter  value  of  n : '))
		for  i  in  range(n):  #  Execute  loop  'n'  times
			large = max(s)  #  Largest  element  of  the  set
			s . remove(large)   #   Removes  largest  element  from  set
		print(F'{n}th  largest  element  :  {large}')
		ch = input('Continue (y / n) ?  :  ') 
		if  ch in  'Nn':
				break
except: #   Executed  when  n >  len(list)
		print('Invalid  input')
