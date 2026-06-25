# Write  a  program  to  print  day  of  the  week  with  match ... case
try:
	m = int(input('Enter  any  day  number  (1 - 7) :  '))  #   2	
	match   m:
		case  1:
			print('Monday')
		case  2:
			print('Tuesday')
		case  3:
			print('Wenesday')
		case  4:
			print('Thursday')
		case  5:
			print('Friday')
		case  6:
			print('Saturday')
		case  7:
			print('Sunday')
		case  _:
			print('Invalid  day  number')
	# End  of  match
	print('Bye')
except:
	print('Input  should  be  an  integer')




'''
What  is   _   called ?  --->  Anonymous  object  (or)  Nameless  object
'''
