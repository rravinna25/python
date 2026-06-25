'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
try:
	digit = int(input('Enter  any  digit  (0 - 9): '))
	if  digit == 0:
		print('Zero')
	else:
		if  digit == 1:
			print('One')
		else:
			if  digit == 2:
				print('Two')
			else:
				if  digit == 3:
					print('Three')
				else:
					if  digit == 4:
						print('Four')
					else:
						if  digit == 5:
							print('Five')
						else:
							if  digit == 6:
								print('Six')
							else:
								if  digit == 7:
									print('Seven')
								else:
									if  digit == 8:
										print('Eight')
									else:
										if  digit == 9:
											print('Nine')
										else:
											print('Not  a  digit')
except:
		print('Input  should  be  an  integer')


'''
What  is  the  issue  when  else  and  if  are  used  instead  of  elif ?  --->  1) Too  many  indentations
																													2) No  readability  and  clarity
																													3) Whole  program  gets  shifed  right
'''
