# Save  in  cwd \ p1 \ __init__ . py file
if  __name__  !=  '__main__':
	import  p1 . mod1 ,  p1 . mod2


'''
1) py  __init__  . py
    What  is  the  value  of  __name__ ?  ---> '__main__'

2) py  __init__  . py	
    What  does  the  command  do ?  --->  Nothing  becoz  if  conditon  is  False

3) import  p1
    What  is  the  value  of  __name ?  --->  Package  name  'p1'

4) import  p1
    What  does  the  import  statement  do ?  --->  Imports  package  p1 ,  executes  __init__  module  and
																			  also  imports  mod1  and  mod2  of  package  p1

5) if  __name__  !=  '__main__':
			import  p1 . mod1 ,   p1 . mod2
    What  is  the  issue  without  'if'  condition ?  --->																	
																		py  __init__ . py  raises  error  becoz  it  searches  for  package  p1  in  p1
																		which  does  not  exist

6) if   __name__  !=  '__main__':
   	      import  p1 . mod1 ,  p1 . mod2
    What  is  the  issue  without  p1  in  p1 . mod1 , p1 . mod2 ?   --->																																	
																   py  reuse . py  raises  error  becoz  mod1  and  mod2  are  searched  in  cwd
																   which  do  not  exist
'''
