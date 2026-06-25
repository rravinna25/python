# Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5)) #  Creates  an  empty  generator  object
g2 = g1  #  Ref  g2  points  to  generator  object  g1
for  y  in  g1:  #  'y'  is  each  element  yielded  by   gen  expression
	print(y)  #  0  <next  line> 1  <next  line>  4  <next  line>  9 <next  line>  16  <next  line>
	time . sleep(1)
for  y  in  g2:   #  Not  executed :  Object  g2  (i.e. g1)  is  fully  iterated  by  1st  for  loop
	print(y)
print(g1  is  g2) # True  :  References  g1 and g2  point  to   same generator object


'''
How  many  generator  objects  are  in  the  program ?  --->  Just  one  object  with  two  references  g1  and  g2
'''
