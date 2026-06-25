#  Find    outputs (Home  work)
def      f1():
	print('One')
	yield    1
	print('Two')
	yield    2
	print('Three')
	yield    3
	print('End')
# End  of  generator
g = f1() #  Creates  an  empty  generator  object
for   m   in   g: #   'm'  is  that  element  yielded  by  generator  function
	print(m)  
x ,  y ,  z  =  f1() #  5  events
print(x)
print(y)
print(z)


'''
One
1
Two
2
Three
3
End
One
Two
Three
End
1
2
3


1) x , y , z = g
    What  are  the  five  events  ?  --->  
	a) Creates  an  empty  generator  object
	b) Executes  generator  function  completely  without  stoping  in  the  middle  even  though  there  are  yield  statements
        Outputs  are   One , Two , Three , End    
	c) Stores  elements  1 , 2  and  3  in  object  'g'    
	d) Unpacks  object  'g'  to  objects  x , y  and  z   
	e) Object  'g'  becomes  empty

2) x , y , z = *g
    Is  the  statement  valid ?  --->  No  becoz  object  is  automatically  unpacked  due  to  multipe  objects  on  left  side
										               of  =  operator  and  hence  *  can  not  be  used

3) What  are  the  two  drawbacks  of  unpacking  generator ?  --->  
														Waiting  time  and  MemoryError  when  there  are  too  many  yield  statements

4) x = f1()
    x , y , z = f1()
    What  is  the  difference ?   --->	 x  = f1()  creates  an  empty  generator  object
													     x , y , z = f1()  creates  a  generator  object  with  three  elements  and  unpacks
'''
