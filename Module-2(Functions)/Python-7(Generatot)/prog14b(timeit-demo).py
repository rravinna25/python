#  Find  outputs
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]' ) )    #  Execution  time  for  storing  500  elements  in  the  list  :  21.43 sec (approx)
print(timeit('( x * x   for  x  in  range(500) )'  ) )   #  Execution  time  for  creating  an   empty  generator  object:  0.17 sec (approx)


'''
1) Observe  that  there  is  no  waiting  time  for  generator

2) 21.83sec  of  time  is   needed   to  store  500  elements  in  the  list  but  it  takes  negligible  time  for  generator  object
'''
