#  How  to  modify  an  element  of  tuple  (without  converting  to  list) ?   (Home  work)
a  =  10 ,  20 ,  30 ,   40 ,  50
#     0      1       2       3      4
#a[2] = 35 # Error :  Tuple  element  can  not  be  modified  as it is  immutable
print(a , id(a)) # (10 , 20 , 30 , 40 , 50)   <space>  Address of  tuple  with  30
a = a[:2] + (35,) + a[3:]  #  Modifies  ref  'a'  to  a  new   tuple  with  35   i.e.  a = (10 , 20) + (35,) + (40 , 50)
print(a , id(a)) # (10 , 20 , 35 , 40 , 50)  <space>  Address of  tuple  with  35


'''
1) Can  tuple  element  be  modified ?  --->  No  becoz  it  is  immutable

2) a = a[ : 2] + (35,) + a[3 : ]
    What  is  modified ?  --->	Reference  but  not  tuple

3) In  other  words,  three  tuples  are  concatenated  to  form  a  new  tuple  and
    reference  'a'  points  to  the  new  tuple
'''
