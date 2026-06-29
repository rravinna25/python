'''
Write  a  program  to  guess  a  number  between   1  and  100000.
1) Print  Too  low  (or)  Too  high  depending  on  input.

2) Print  the  number  and  number  of  attempts
'''
import  random
low = 1
high = 100000
rand =  random . randint(low , high)  #  Any  random  number  between  1  and  100000  
ctr = 0
while  True:  
	inp  =  int(input(F'Enter  any  number  between  {low}   and  {high}  :  '))  
	ctr += 1   #  Counts  number  of  attempts
	if  inp  ==  rand:
		print(F'Guessed  {inp}  in  {ctr}  attempts')
		break  #  Get  out  of  the  loop
	elif  inp < rand:		
		print('Too  low  , try  again')
		low = inp + 1
	else:
		print('Too  high  , try  again')
		high = inp - 1  
