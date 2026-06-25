# Find  outputs (Home  work)
import  time
g = (x * x   for  x  in  range(5))  #  Creates  an  empty  generator  object
for  y  in   g:  #  'y'  is  each  element  yielded  by  generator  expression
	print(y)  #   0  <next  line>   1  <next  line>  4  <next  line>  9 <next  line>  16 <next  line>
	time . sleep(1)
	print('Hello')
for  y  in   g:   #  Not  executed  :  Object  'g'  is   fully  iterated  by  1st  for  loop
	print(y)



'''
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
'''

'''
1) How  many  times  can  a  generator  object  be  iterated ?  ---> Just  once
    What  about  sequence ?  ---> It  can  be  iterated  multiple  times

2) g = (x * x   for    x    in    range(5))
    for   y  in   g:
	      pass
    for   y  in   g:
	      pass
    Why  is  2nd  for  loop  not  executed ?  ---> Since  1st  for  loop  has  iterated  object  'g'  fully  and
																		  hence  2nd  for  loop  raises  StopIteration  error  in  1st  iteration  itself
'''
