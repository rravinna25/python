# Find  outputs  (Home  work)
def  f1(x , y):
	if   x > 40:
		return  #  Moves  out  of  the  function
	x += y
	f1(x , y) # Address  of  next  statement  is  saved  in  the  stack  along  with  formal  parameter  values  before  control  moves  to  same  function  f1()
	print(x)
# End  of  the  function
x = 10
f1(x , x := x + 1)  #  f1(10 , 11)  i.e.  Address  of  next  statement  is  saved  in  the  stack  before  control  branches  to  function  f1()
print(x)  #  11


'''
43
32
21
11


1) What  are  saved  in  the  stack  when  a  function  is  called ?  --->
																		Address  of  next  statement  and  values  of  formal  parameters

2) What  happens  after  function  terminates ?  --->   Values  saved   in  the  stack  are  restored  into  formal  parameters
                                                                                      and  execution  resumes  from  the  address  saved  in  the  stack
'''
