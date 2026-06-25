# What  are  the  outputs  if  input  is  {10 , 20 , 15 , 18 , 20 , 12 , 18}
a = input('Enter  Set  :  ')  #  Reads  string  string
print(a) #  '{10 , 20 , 15 , 18 , 20 , 12 , 18}'  in same  order  with  duplicates  as  it  is  a  string
print(type(a)) # <class 'str'>
b = eval(a) #  Converts  string  set  to  set
print(b) # {10 , 20 , 15 ,  12 , 18}  in  any  order
print(type(b)) # <class 'set'>


'''
1) Let  input  be  {10 , 20 , 15 , 18 , 20 , 12 , 18}
    What  does  input()  function  read ?  --->  string  set  i.e.  '{10 , 20 , 15 , 18 , 20 , 12 , 18}'
    What  does  eval('{10 , 20 , 15 , 18 , 20 , 12 , 18}')  do ?  ---> Converts  string  set  to  set   i.e. {10 , 20 , 15 , 18 , 12}

2) Let  input  be  set(),
    What  does  input()  function  read ?  ---> 'set()'
    What  does  eval('set()')  do ?  ---> Converts   'set()'  to  set()
'''
