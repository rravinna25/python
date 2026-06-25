'''
Write  a  generator  to  divide  a  string  into  words

Hint1:  Use  generator  function  and  for   loop

Hint2:  Use  split()  method  of  str  class
'''
import time
def   f1(s):
	list = s . split()  #  Divides  string  into  list  of   strings  based  on  white  space  delimeter
	for  x  in  list:  #  'x'  is  each  element  of  the  list
		yield   x  #  yields  the  word  to  for  loop  variable   'y'
# End of generator
s = input('Enter  any   string  :  ')
g = f1(s)  #  Creates  an  empty  generator  object
print('Words  of  the  string')
for  y  in   g:  #  'y'  is  that  word  which  is  yielded  by   generator  function
	print(x)  #  Each  word  of  the  sentence
	time . sleep(1)
