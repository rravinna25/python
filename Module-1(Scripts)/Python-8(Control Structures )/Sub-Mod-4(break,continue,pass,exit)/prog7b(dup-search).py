'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

What  are  the  outputs ?  --->   15  is  found  at  index  2
												   15  is  found  at  index  5
												   15  is  found  at  index  8
												   15  is  found   3  times
'''
a = eval(input('Enter any list: '))
x = eval(input('Enter the element to be searched : '))
for  i  in  range(len(a)):
	if  a[i] == x:
		print('Found  at   index  :  ' ,  i)		
else:
	print('Not  Found')
