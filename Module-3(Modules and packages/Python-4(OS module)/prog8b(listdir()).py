'''
Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory

Input :  Directory  (or)  path

Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
'''
import   os
try:
	dir = input('Enter  directory  name (or) path :  ')  #  Reads  a  directory  name  (or)  path
	list  =  os . listdir(dir)  #  List  of  all the  file and  sub-directories  of  user  input  directory
	a  = b = []  #  Empty  list
	for  x  in  list:  #  'x'  is  each  element  (i.e.  file  (or)  sub-dir) of   the  list
		if  '.'  in  x:  #   Is  'x'  a  file  (file  contains  '.'  but  not  directory)
			a . append(x)  #  Appends  file  'x'  to  list  'a'
		else:
			b . append(x)  #  Appends  directory  'x'  to  list  'b'
	print('List  of  the  files :  '  , a)
	print()
	print('List  of  the  directories :  '  , b)
except  FileNotFoundError:
	print(F'Directory  {dir}  does  not  exist')
