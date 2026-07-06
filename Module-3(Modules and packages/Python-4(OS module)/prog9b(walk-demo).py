# Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
import  os
g =  os . walk('sairam')  #  Returns  an  empty  generator  object
while  True:
	try:
		tpl = next(g)  #  Returns  a  tuple  of  3  elements
		print('Directory  Path : ' , tpl[0])
		print('Sub  Directories : ' , tpl[1])
		print('Files : ' , tpl[2])
		os . system('pause')  #  Prints  next  tuple  after  user  strikes  a  key
		os . system('cls')   #  Clears  existing  tuple  before  printing  next  tuple
	except  StopIteration:
		break


'''
1) How  to  use  for  loop  instead  of  while  loop ?  --->  for  tpl  in  g:
																							   print('Directory  Path : ' , tpl[0])
																							   print('Sub  Directories : ' , tpl[1])
																							   print('Files : ' , tpl[2])
																							   os . system('pause') 
																							   os . system('cls')   
																							   
2) How  to  use  for  loop  in  another  way ?  --->  for  a , b ,  c  in   g:
																							   print('Directory  Path : ' , a)
																							   print('Sub  Directories : ' , b)
																							   print('Files : ' , c)
																							   os . system('pause') 
																							   os . system('cls')
'''
