# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
g = f1()  #  Creates  an  empty  generator  object
for  x  in  g:  #   'x'  is  each  element  yielded  by  generator  function
	print(x)  #  25  <next  line>  10.8  <next  line>  Hyd  <next  line>
for  x  in  g:  #  Not  executed  :  Generator  is  fully  iterated 
	print(x)
for  x  in  g:  #  Not  executed  :  Generator  is  fully  iterated 
	print(x)


'''
1) for  x  in   generator:
	      statements
    for  x  in   same-generator:
	      statements
    for  x  in   same-generator:
	      statements
    Are  2nd  and  3rd  for  loop  execucted ?  --->  No  becoz  generator  object  is  already  fully  iterated  by  1st  for  loop
																			   and  hence  2nd  and  3rd  for  loops  raises  StopIteration  in 
																			   1st  iteration  itself

2) How  many  times  can  a  generator  be  iterated ?  --->  Only  once

3) list = [25 , 10.8 , 'Hyd', True]
    for  x  in  list:
		 print(x)
    for  x  in  list:
		 print(x)
	for  x  in  list:
		 print(x)
    Are  2nd  and  3rd  for  loop  execucted ?  --->  Yes  becoz  sequence  can  be  iterated  multiple  times
'''
