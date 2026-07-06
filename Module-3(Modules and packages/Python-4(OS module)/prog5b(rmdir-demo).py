'''
Write  a  program  to  delete  a  directory.
Input  is  directory  name  (or)  path  of  the  directory
'''
import   os
try:
	dir = input('Enter  directory  name  (or)  path :  ')
	os . rmdir(dir)  #  Removes  a  directory
	print(F'Directory  {dir}  is  removed')
except  FileNotFoundError:
	print(F'Directory  {dir}  does  not  exist')
except  OSError:
	print(F'Directory  {dir}  is  non-empty  and  can  not  be  removed')


'''
1) Can  OSError  be  handled  before  FileNotFoundError ?  --->   No  becoz  OSError  is  parent  class  to  FileNotFoundError

2) In  other  words,  child  error (i.e FileNotFoundError)  should  be  handled  before  parent  error (i.e. OSError)

3) What  happens  when  OSError  is  handled  before  FileNotFoundError ?  --->																	
														OSError  except  suite  is  executed  even  when  try  suite  raises  FileNotFoundError  
'''
