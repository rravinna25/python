'''
Write   a  function  to  test  a  number  is  prime  (or)  not.
1) What  is  a  prime  number ?  ---> A  number  without  divisors  except  1  and  itself

2) Let  input  be  25
    What  is  the  range  of  divisors ? ---> i =   2 , 3 , 4 , 5 , 6 , .....  12

3) Let  input   be  11
    What  is   the  range  of  divisors ? ---> i =  2 , 3 , 4 , 5

4) What  action  to  be  made  if  'i'  is  not  a  divisor  of  input  number ?  ---> Move  to  the  next  element  of  range  object

5) What  action  to  be  made  if  'i'  is  a  divisor  of  input  number ?  --->  return   False

6) What  action  to  be  made  if  there  are  no  divisiors  to  input  number  ? ---> return  True  outside  the  loop
'''
def   prime(n):
	for   i    in   range(2 , n // 2 + 1):  #  Range  of  divisions  is  2  to  n // 2
		if  n % i == 0: # Is  'i'  a  divisor  of  'n'
			return  False #  'n'  is  not  prime
	#  End  of  for  loop
	return  True  #  'n'  is  prime
'''
1) prime(25)  --->  False
    How  many  times  is  for  loop  executed ?  --->  4  times

2) prime(11) --->  True
    How  many  times  is  for  loop  executed ?  --->  4  times

3) prime(2) ---> True
    How  many  times  is  for  loop  executed ?  ---> 0  times

4) prime(49) --->  False
    How  many  times  is  for  loop  executed ?  --->  6  times

5) range(2 , n / 2 + 1)
    What  is  the  issue ?  --->  /  is  a  float  operator  but  range()  can  not  have  float  arguments

6) for  i  in  range(2 , n // 2 + 1):
	    if  n % i == 0:
				return   False
	   else:
   	            return  True
    What  are  the  two  issues  with  else ?  --->  Executes  for  loop  only  once  and
								                                             prime(25)  returns  True  even  though  25  is  not  a  prime  number

7) for  i  in  range(1 , n // 2 + 1):
	    if  n % i == 0:
				return   False
     What  is  the  issue  with  1  in  range() ? --->  Every  number  is  divisible  with  1  and  hence  do  not  start  from  1
																			  i.e. Start  from   2 

8) for  i  in  range(2 , n):
	    if  n % i == 0:
				return   False
    What  is  the  issue  with  'n'  in  range() ? ---> There  are  no  divisors  beyond  n //  2  and  hence  do  not  proceed  upto  n - 1
'''
if   __name__  ==  '__main__':
	n = int(input('Enter  any  integer  number  :  '))
	if  n < 2:  #  1  is  neither  prime  not  composite
		print('Invalid  input')
	elif  prime(n):  #  Is  'n'  prime  number
		print('Prime  number')
	else:
		print('Composite  number')

