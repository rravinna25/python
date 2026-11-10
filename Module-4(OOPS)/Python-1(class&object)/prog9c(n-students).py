'''
Repeat  student  program  for  'n'  students

1) Reuse  Student  class  defined in  prog9a  but  do  not  rewrite

2) Use  list  of  objects
'''
from  prog9a  import  student  #  Imports  student  class  and  the  if  statement  outside  the  student  class  in  prog9a
n = int(input('How  many  students ?  :  '))  #  Read  number  of  students  to   variable  'n'
a = []   #  Empty  list
for  i  in  range(n):  #  Appends  'n'  student  class  objects  to   list  'a'
	s = student()  #  Creates  an  empty  student  class  object
	a . append(s)  #  Appends  object  's'  to list  'a'
i = 1
for  s  in   a:   #  's'  is  each  student  class  object  of  list  'a'
	print(F'Student  {i}')
	s . get()  #  Adds  variables  rno , sname , gender   and  list  'm'  to  object  's'  with  user  inputs
	s . compute()  #  Adds  variables  tot , avg  and  grade  to  object  's'  with  results
	i += 1
for  s  in  a:  #  's'  is  each  student  class  object  of  list  'a'
	print(s)  #   __str__()  method  returns  values  of  object  's'  in  the  form  of  string



'''
1) How  many  objects  are  in  list  'a'  ?  ---> 'n'  Student  objects

2) What  are  the  names   of  objects  ?  --->  a[0] , a[1] , a[2]  and  so  on

3) s = student()
    a . append(s)
    How  to  combine  the  two  statements  to  a  single  statement ?  ---> a . append(student())

4) for  s  in   a:
			s . get()
			s . compute()
			print(s)
   What  is  the  issue  with  the  above  for  loop ?  --->   Immediate  results  i.e.  Current  student  results  are  printed  before
															                             next  student  inputs  are  entered

5) Therefore  two  for  loops  are  needed  to  obtain  delayed  results  in  tabular  form

6) When  is  disp()  method  recommended ? --->  To  print  single  student
    When  is  __str__()  method  recommended ? --->  To  print  multiple  students

7) i = 1
    for  s  in  a:
			print(f'Student  {i}')
			s . get()
			s . compute()
			i += 1
    How  to  use  indexed  based  for  loop  in  stead  of  for  .... each  loop ?  --->  for  i  in  range(n):
																																	   print(f'Student  {i + 1}')
		                                                                                                                               a[i] . get()
		                                                                                                                               a[i] . compute()

8) What  is  each  object  name  in  indexed  based  for  loop ?  --->  a[i]
     What  is  each  object  name  in  for  ... each  loop ?  --->   s
'''
