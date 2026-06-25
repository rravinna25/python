'''
Write  a  program  to  print  all  the  rotations  of  the  string

Input : SPACE
    
What  are  the  outputs ?  --->  SPACE
										          PACES
												  ACESP
												  CESPA
												  ESPAC
'''
a = input('Enter any string :  ') #   Reads  string
print('Rotations')
for  i   in  range(len(a)):  #  Executes  loop  length  times  as  there  are  length  number  of  rotations
		print(a) #   Prints  each  string
		a = a[1:] + a[0]  #   Modifies  ref  'a'  to  the  next  string
		
		
'''
a = 'SPACE'
What  does  a[1:]  do ?  --->  Returns  same  string  without  first  character
What  does  a[0]  do ?  --->  Returns  first  character
'''
