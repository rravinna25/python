'''
Write  a  program  to  rename  a  file  and  directory

Input  is  filename  (or)  directory  name
'''
import  os
try:
	fname1 = input('Enter  1st  fllename :  ')
	fname2 = input('Enter  2nd  fllename : ')
	os . rename(fname1 , fname2)
	print(F'File  {fname1}  is  renamed  to  {fname2}')
except  FileExistsError:
	print(F'File  {fname2}  exists')
except  FileNotFoundError:
	print(F'File  {fname1}   does  not  exist')

	
	
'''
Can  the  order  of  except  suites  be  changed  ?  --->   Yes  becoz  FileExistsError  and  FileNotFoundError  are  not  related
'''
