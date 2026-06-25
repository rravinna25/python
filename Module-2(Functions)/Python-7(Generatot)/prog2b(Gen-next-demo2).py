# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
while  True:
	print(next(f1()))  #   25  ,  25  ,   25  , ........


'''
1) What  does  next(f1())  do ?  --->  f1()  creates  an  empty  generator  object  
																			and  
														 next(generator-object)  yields  first  element  25

2) How  many  generator  objects  are  in  the  program  and  why?  --->
													Infinite  as  every  call  to  f1()  in  each  iteration  creates  a  new  generator  object

3) Why  is  same  25  yielded  every  time ?  --->  Since  each  iteration  of  while  loop  creates  a  new  generator  object  and
									                                          next(new-gen-obj)  yields  the  first  element  25

4) g = f1()
    while   True:
	     	 print(next(g))
    How  many  generator  objects  are  in  the  above  code ? ---> Only  one  which  is  created  before  the  loop
    What  are  the  outputs ?  --->  25   10.8    Hyd    StopIteration  error
    Why  is  25  not  yielded  every  time ?  ---> Since  it  is  the  same  generator  object  but  not  a  new  generator  object
'''
