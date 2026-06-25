# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a)) # True  :  2nd  element  of  list  'a'  is  True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b)) # False :  All  the  elements   of  list  'b'  are   False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))  # True  :  4th  element  of  list  'c'  is   25  i.e.  True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d)) # False :  All  the  elements   of  list  'd'  are   False
e = []
print(any(e)) # False :  No  True  elements  in  list  'e'


'''
any()   function
-------------------
1) What  does  any(list)  do ?  --->  Returns  True  when  at  least  one  element  of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  every  element  of  the  list  is  false

3) if  cond1  or  cond2  or  cond3  or  cond4:
     How  to  reduce  the  four  conditions  to  a  single  condition ?  --->   if  any([cond1 , cond2 , cond3 , cond4]):

4) all()  and  any()  functions  are  used  as  an  alternative  when  there  are  too  many  conditions  in  if  and  while
'''
