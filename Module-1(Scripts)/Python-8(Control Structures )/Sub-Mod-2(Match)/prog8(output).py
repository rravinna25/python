'''
1) What  are  the  outputs  if  input  is  -6 ? --->  Hyd  <next  line>  Sec <next  line>  Cyb  <next  line>  Bye  <next  line>
2) What  are  the  outputs  if  input  is  15  ?  --->  One  <next  line> Two  <next  line>  Three <next  line>  Bye  <next  line>
3) What  are  the  outputs  if  input  is  10.8  ?  --->  India  <next  line>  China  <next  line>  Usa  <next  line>  Bye  <next  line>
4) What  are  the  outputs  if  input  is  0  ?  --->  Hyd  <next  line>  Sec <next  line>  Cyb  <next  line>  Bye  <next  line>
5) What  are  the  outputs  if  input  is  -10  ?  --->  One  <next  line> Two  <next  line>  Three <next  line>  Bye  <next  line>
6) What  are  the  outputs  if  input  is  7  ?  --->  Hyd  <next  line>  Sec <next  line>  Cyb  <next  line>  Bye  <next  line>
'''
x = eval(input('Enter any  number :  '))
match  x:
	case  7 |  -6  |  0:  #  Executed  when  'x'  is   7 , -6  (or)  0
		print('Hyd')
		print('Sec')
		print('Cyb')
	case  -10 | 15:  #  Executed  when  'x'  is   -10  (or)  15
		print('One')
		print('Two')
		print('Three')
	case  _: #  Executed  when  'x'  is  none  of  the  above  5  values
		print('India')
		print('China')
		print('Usa')
# End  of  match
print('Bye')


'''
What  is  '|'  operator  called ?  --->  Bitwise  or  operator
'''
