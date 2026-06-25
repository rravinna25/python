'''
Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse  directions  without  slice

       	     				  0      1     2      3     4
Let  input  be		  V     A     M     S     I
			        		 -5    -4    -3    -2    -1

What  are  the  outputs ?  --->  Character  at  index  0  :  V
								                 Character  at  index  1  :  A
								                 Character  at  index  2  :  M
							                     Character  at  index  3  :  S
								                 Character  at  index  4  :  I

								                 Character  at  index  -1  :  I
								                 Character  at  index  -2  :  S
								                 Character  at  index  -3  :  M
								                 Character  at  index  -4  :  A
								                 Character  at  index  -5  :  V

Hint:  Use  two  for  loops
'''
a = input('Enter the string: ')
print('String  from  left  to  right : ')
for  i  in  range(len(a)):
	print(F'Character  at  index  {i} : {a[i]}')  #   prints  a[i]  where  'i'  varies  from  0  to  length - 1
print('String  from  right  to  left: ')
for  i  in  range(1 , len(a) + 1):
	print(F'Character  at  index  {-i} :  {a[-i]}')   #   prints  a[-i]  where  'i'  varies  from  1  to  length
