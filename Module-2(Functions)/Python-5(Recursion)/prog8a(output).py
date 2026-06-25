#   Find  outputs
def  f1():
	global  a  #  Treats  'a'  as   global  variable
	if  a:
		print(a)
		a = a - 1
		f1()  #  Address  of  next  statement  is  saved  in  the  stack  before  control  moves  to  same  function  f1()
		print('Hello')
		print('Hi')
		print(a)
	#  End  of  if  statement		
	print('Bye')
# End  of  the  function
a = 3 #   Creates  global  variable  with  value  3
f1() #  Address  of  next  statement  is  saved  in  the  stack  before  control  branches  to  function  f1()
print('End')


'''
3
2
1
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
Hello
Hi
0
Bye
End
'''
