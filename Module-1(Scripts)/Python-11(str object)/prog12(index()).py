# index()  method   demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
i = -1  
while  True:
	try:
		i = a . index('is' , i + 1)  #   Index  of  each  'is'   in  object  'a'
		print(i)  #  Index  of   each  'is'  in  object  'a'  i.e.  4  ,  23 ,  42 ,  46
	except:  #  Executed  when  there  is  no  more  'is'
		break  #  Get  out  of  the  loop
print('End')


'''
index()  method
-------------------
It  is  same  as  find()  method  except  that  it  throws   error (but  not  -1) when  string  is  not  found

Syntax :  Same  as   find()  method
'''
