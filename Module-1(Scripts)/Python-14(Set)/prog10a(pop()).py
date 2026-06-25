# pop()  method  demo  program  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {'Hyd' , 25 , True , 10.8}  in  any  order
print(a . pop())  #  Removes  first  element  of  set  and  returns  the  deleted  element i.e.  Hyd
print(a . pop())   #  Removes  first  element  of  set  and  returns  the  deleted  element i.e.  25
print(a . pop())  #  Removes  first  element  of  set  and  returns  the  deleted  element i.e.  True
print(a . pop())   #  Removes  first  element  of  set  and  returns  the  deleted  element i.e.  10.8
#print(a . pop()) # Error :  Cannot  delet  from  an  empty set
print(a) # set()  i.e.  empty  set
b = {10 , 20 , 30 , 40}
#print(b . pop(2)) # Error :  pop()  expects  zero  args 



'''
pop()  method
----------------
1) What  does  pop(No-args)  method  do ?  --->  Removes  first  element  of  the  set  and  returns  the  deleted  element

2) What  does  emptyset . pop()  do ?  ---> Throws  error

3) Is  set . pop(index)  valid ?  --->  No  becoz  set  is  not  indexed

4) How  many  arguments  can  pop()  method  take  ?  --->  Zero
'''
