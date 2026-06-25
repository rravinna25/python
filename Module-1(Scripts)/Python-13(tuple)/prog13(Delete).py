# How  to  delete  an  element  of  tuple ?  (Without  converting  to  list) (Home  work)
a  = 10 , 20 , 30 , 40 , 50
#    0     1      2     3      4
#a . remove(30) # Error : No  remove()  method  in tuple
#del  a[2] # Error :  Tuple element  can  not be  deleted  as tuple  is  immutable
#a . pop(2) # Error : No   pop()  method  in tuple
print(a , id(a)) # (10 , 20 , 30 , 40 , 50)  <space> Address  of  5-element  tuple 
a = a[:2] + a[3:]  #  a = (10 , 2) + (40 , 50)
print(a , id(a)) #(10 , 20 , 40 , 50)  <space> Address of  4-element  tuple  


'''
1) Can  tuple  element  be  removed ?  --->  No  becoz  tuple  is  immutable

2) a = a[ : 2] + a[3 : ]
    What  is  modified ?  --->	Reference  but  not  tuple

3) In  other  words, two  tuples  are  concatenated  to  form  a  new  tuple  and  reference  is  modified  to  new  tuple
'''
