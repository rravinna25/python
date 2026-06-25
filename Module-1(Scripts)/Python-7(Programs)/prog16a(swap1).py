'''
(Home  work)
Write  a  program  to  swap  values  of  two   objects   using  3rd  object

Let  x = 10  and  y = Hyd
What  are  the  values  of  x  and  y  after  swap ?  --->   x = Hyd  and   y = 10
'''
x = input('Enter  1st  input  : ')
y =  input('Enter  2nd  input  : ')
print(F'Before  swap :  {x=}  \t  {y=}')
temp = x
x = y
y = temp
print(F'After  swap :  {x=}  \t  {y=}')
