# Find  outputs (Home  work)
a = (10 , 20 , 30)  #  Ref  'a'  points   to  tuple  of  3  elements
print(a) # (10 , 20 , 30)
print(id(a)) #  Address of  tuple with  3  elements  (may  be  1000)
a = a * 2  #  Ref  'a'  is  modified  to  another  tuple of  6  elements
print(a) #  (10 , 20 , 30 , 10 , 20 , 30)
print(id(a)) #  Address of  tuple with  6  elements  (may  be  2000)


'''
1) a = (10 , 20 , 30)
    a = a *  2
    What  is  modified ?  ---> Reference  but  not  tuple

2) What  happens  to  3-element  tuple  when  ref  'a'  is  modified  to  6-element  tuple ?  --->
																									Gets  deleted  by  pvm  as  there  is  no  reference  to  it
'''
