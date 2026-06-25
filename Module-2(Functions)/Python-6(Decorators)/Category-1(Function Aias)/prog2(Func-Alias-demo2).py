# Find  outputs (Home  work)
p = print  #   Reference  'p'  points   to  print()  function
p('Hyderabad')  #   Executes  function  print  thru  ref  'p'  which  prints  'Hyderabad'
print = None  #  Ref  print  points  to  object  None
#print('Hello') #  Error : None('Hello')  --->  None  can  not be  called  as  it  is   not  a  function
p('Hello')  #   Executes  function  print  thru  ref  'p'  which  prints  'Hello'


'''
Hyderabad
Hello
'''
