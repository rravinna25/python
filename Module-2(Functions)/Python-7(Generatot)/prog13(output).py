# Find  outputs
def   f1():
        yield   [10 , 20]  #  Yielded  to   for  loop  variable  'x'
        yield  {30 , 40 , 50}   #  Yielded  to   for  loop  variable  'x'
        yield  60  , 70 , 80 , 90   #  Yielded  to   for  loop  variable  'x'
        yield  100   #  Yielded  to   for  loop  variable  'x'
# End  of  generator
g = f1()  #  Creates  an  empty  generator  object
for   x   in   g:  #  'x'  is  that  object  which  is  yielded  by  generator  function
	print(x)   #  Each  object  yielded  by  generator
	print(type(x))


'''
[10 , 20]
<class 'list'>
{30 , 40 , 50} in  any order
<class 'set'>
(60  , 70 , 80 , 90)
<class 'tuple'>
100
<class 'int'>
'''


'''
1) What  does  generator  yield  for  the  1st  time ?  --->  [10 , 20]

2) What  does  generator  yield  for  the  2nd  time ?  --->  {30 , 40 , 50}

3) What  does  generator  yield  for  the  3rd  time ?  ---> (60, 70 , 80 , 90)

4) What  does  generator  yield  for  the  4th   time ?  --->  integer  100

5) What  does  generator  yield  for  the  5th   time ?  --->  Raises  StopIteration  error  as  nothing  is  yielded
'''
