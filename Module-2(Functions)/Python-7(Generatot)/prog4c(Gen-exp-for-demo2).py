# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):  #   Creates  1st  generator  object  which  is  iterated  with  for  loop
	print(y) #  0  <next  line> 1  <next  line>  4  <next  line>  9 <next  line>  16  <next  line>
	time . sleep(1)
for  y  in   (x * x   for    x    in    range(5)):  #   Creates  2nd  generator  object  which  is  iterated  with  for  loop
	print(y) #  0  <next  line> 1  <next  line>  4  <next  line>  9 <next  line>  16  <next  line>
	time . sleep(1)


'''
How  many  generator  objects  are  in  the  program ?  --->  2
'''
