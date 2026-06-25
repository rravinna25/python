# What  is  the  advantage  of  generator ?
import  time
g  =  (x * x   for  x   in   range(1000000000000000000000000000000000000000000000000000000000000000)) #   Creates  an  empty  generator  object  but  does  not  store  any  element  in  generator
while   True:
	try:
		print(next(g))  #   Each  element  of   generator
		time . sleep(0.5)
	except:
		break

'''
Advantages  of  generator
------------------------------
1) What  are  two  advantages  of  generator ?  ---> 
    No  waiting  time:  Elements  are  yielded  as  and  when  they  are  needed  but  not  in  advance.
					             Therefore  there  is  no  waiting  time  as  elements  are  generated  on   'fly'
   No  memory  error:  Elements  are  yielded  one  at  a  time  but  not  all  simultaneously

2) When  is  generator  recommended  ?  ---> When  too  many  elements  are  to  be  processed
'''
