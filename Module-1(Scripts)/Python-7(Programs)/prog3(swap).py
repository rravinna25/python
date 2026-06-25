'''
Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object

Let  'x'  be  25  and  'y'  be   'Hyd'
What  are  'x'  and  'y'  after  swap ?  ---> Hyd  and  25

Hint:  Swap  references  but  not  objects
'''
x = input('Enter  1st  input :  ')
y = input('Enter  2nd  input : ')
print(F'Before  swap :  {x=}  \t  {y=}')
x , y = y , x  #   Ref  'x'  points  to  object 'y' and  at  the  same  time   ref  'y'  points  to  object  'x'
print(F'After  swap :  {x=}  \t  {y=}')



'''
1) x , y = y , x
   What  are  modified (References  (or)  objects) ?  --->  References

2) Both  the  references  x  and  y  are  modified  at  the  same  time

3) Why  are  objects  not  swapped ?  --->  Since  inputs  are  strings  which  are  immutable  objects
'''
