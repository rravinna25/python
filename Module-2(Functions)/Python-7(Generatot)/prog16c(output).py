#  Find  outputs
g = (x * x  for  x  in  range(500000000000000000))  #  Creates  an  empty  generator  object
print(*g) # Waiting  time  and  memory  error  due  to  too  many  elements



'''
What  are  the  four  events  for  *g ?  --->   1) Executes  generator  expression  without  stopping  in  the  middle
																	  2) Stores  0 ^ 2 , 1 ^ 2 , 2 ^ 2 , ....   in  generator  object  'g'																	 
																	  3) Unpacks  generator  object  to  0 , 1 , 4 , 9 , ....																     
																	  4) Generator  object  becomes  empty
'''
