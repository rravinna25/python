# Identify  error
if  { }:
{   #  Error :  {  is  not  permitted  for  suite
	print('One')
	print('Two')
	print('Three')
} #  Error :  }  is  not  permitted  for  suite
else:
{  #  Error :  {  is  not  permitted  for  suite
	print('Four')
	print('Five')
	print('Six')
} #  Error :  }  is  not  permitted  for  suite
print('Bye')


'''
Can  statements  of  if  suite  and  else  suite  be  in  braces ?  --->
							No  becoz  braces  are  used  for  set  and  dictionary  but  not  for  suite (i.e.  statements)
'''
