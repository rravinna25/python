# Find  outputs
def  f1():
	a = 3  #  Creates  a  Lv  with  value  3
	if  a:
		print(a)
		a = a - 1
		f1()  #  Address  of  next  statement  is  saved  in  the  stack   before  control  branches  to  the  same   function
		print('Hello')
		print('Hi')
		print(a)
	print('Bye')
# End  of  the  function
f1()
print('End')



'''
3
3
3
and  so  on  until  stack  is  full
RecursionError
'''
