'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																																Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  --->  Print  found   message  along  with  index  and
																														 do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->  Print  not  found   message

6) Hint: Use  for  loop
'''
a = eval(input('Enter any list: '))
x = eval(input('Enter the element to be searched : '))
for  i  in  range(len(a)):
	if  a[i] == x:
		print('Found  at   index  :  ' ,  i)
		break
else:
	print('Not  Found')




'''
1) What  are  the  two  issues  without  break ? --->
	a) Searches  for  'x'  in  rest  of  the  list  even  though  'x'  is  already  found  in  the  list
	   (program  execution  becomes  slow)
	b) Prints  Not  Found  msg  after  for  loop  terminates

2) What  is  the  issue  without  else ?  --->  Prints  both  Found  and  Not  Found  messages 

3) What  is  the  issue  when  else  is  indented  with  if  ?  --->
												Prints  Not  Found  in  each  iteration  of  for  loop  until  element  is  found  in   the  list
'''
