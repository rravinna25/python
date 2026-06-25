# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a)) # True :  All  the  elements  of  list  'a'  are  True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b)) # False :  2nd  element  of  list  'b'  is   False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c)) # False :  3rd  element  of  list  'c'  is   ''  i.e. False
d = [10 , 0 , 20]
print(all(d)) # False :  2nd  element  of  list  'd'  is   0  i.e.  False
e = []
print(all(e)) #  True  :   No  False  elements  in  list  'e'


'''
all()  function
-----------------
1) What  does  all(list)  do ?  --->  Returns  True  when  every  element of  the  list  is  True  and  False  otherwise

2) When  does  it  return  False ?  --->  When  at  least  one  element  of  the  list  is  False

3) if  cond1  and  cond2  and  cond3  and  cond4:
    How  to  reduce  the  four  conditions  to  a  single  condition ?  --->  if  all([cond1 , cond2 , cond3 , cond4]):
'''
