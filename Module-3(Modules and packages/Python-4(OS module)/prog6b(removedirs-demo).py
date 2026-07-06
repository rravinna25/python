'''
Write  a  program  to  delete  a  group  of  directories
Input  is  directory  path
'''
import   os
try:
	dir = input('Enter  path  of  directory :  ') 
	os . removedirs(dir)
	print('Directory  (or)  directories  are  removed')
except  FileNotFoundError:
	print(F'Directory  {dir}  does  not  exist')
except  OSError:
	print(F'Directory  {dir}  is  non-empty')
	