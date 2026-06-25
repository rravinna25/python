'''
Write  a  program  to  merge  two  strings  to  form  a  new  string

1) Let  inputs  be    HYD   and   VAMSI
   What  is  the  output  ?  --->  HVYADMSI

             0     1    2
a  --->   H     Y    D

              0    1     2     3    4
b  --->    V    A    M    S    I


i       a[i]        b[i]          c
--------------------------------------------------------
                                    ''
0      'H'        'V'          '' + 'H' + 'V' = 'HV'

1      'Y'        'A'          'HV' + 'Y' + 'A' = 'HVYA'

2      'D'       'M'          'HVYA' + 'D' + 'M' = 'HVYADM'
--------------------------------------------------------
Concatenate  remainging  characters   of  the  other  string  to  object  'c'
What  is  the  final  result ?  --->  'HVYADMSI'

Hint:  Use  single  while  loop  and  slice
'''
try:
	a = input('Enter  first  string  :  ')
	b = input("Enter  second  string  :  ")
	c = ''
	i = 0
	while  True:  #  Repeat  until  at  least  one  string  is  eachusted
		c  += a[i] + b[i]  #   Concatenates  each  char  of  the  two  strings  to  object  'c'
		i += 1  #  Move  to  next  char
except:
	print('Result  :  ' , c + a[i:] + b[i:])  #  Concatenate  remaining  chars  of  the  two  strings  to  object  'c'



'''
1) What  is   the  difference  between  a[i]   and  b[i] ? --->  a[i]  is  each  character  of  1st  string  and
																						       b[i]  is  each  character  of  2nd  string
																							 
2) What  is   the  difference  between  a[i:]   and  b[i:] ? --->  a[i:]  is  1st  string  without  first  'i'  characters  and
                                                                                                 b[i:]  is  2nd  string  without  first  'i'  characters 
																						      
'''
