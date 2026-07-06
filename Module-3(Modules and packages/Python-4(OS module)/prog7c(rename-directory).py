# Write  a  program  to  rename  a  directory
import  os
try:
	dirname1 = input('Enter  1st  directory  name  :  ')   
	dirname2 = input('Enter  2nd  directory  name :  ')   
	os . rename(dirname1 , dirname2)
	print(F'Directory  {dirname1}  is  renamed  to  {dirname2}')
except  FileExistsError:
	print(F'Directory  {dirname2}  exists')
except  FileNotFoundError:
	print(F'Directory  {dirname1}   does  not  exist')
