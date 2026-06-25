#  Find  outputs  (Home  work)
print({[10 , 20 , 30]}) #  Error :  Set  can not  have  list  as   list  is  mutable
print({{10 , 20 , 30}})  #  Error :  Set  can not  have  set  as   set  is  mutable
print({{}}) #  Error :  Set  can not  have   dict  as   dict  is  mutable
print({(10 , 20 , 30)}) #  {(10 , 20 , 30)}  i.e.  set  can  have  tuple  as  tuple  is  immutable
#print({(10 , 20 , [30 , 40] , 50 , 60)})   # Error :  Even  inner  most  elements  can  not  be  mutable


'''
1) Is  nested  set  valid ?  ---> No

2) What  is  the  issue  with  nested  set ?  --->  Set  can  not  hold  mutable  elements  such  as  list , set  and  dictionary

3) Which  elements  can  set  hold  ?  --->  Immutable  elements  such  as  int , float , str , tuple  and  so  on

4) Why  set  can  not  hold  mutable  elements ?  --->   Since  set  elements  can  not  be  modified  but  mutable  elements
														                             can  be  modified (contradiction)
																					 
5) Can  set  hold  tuple  and  tuple  hold  list ?  ---> No

6) In  other  words,  inner  most  objects  also  can  not  be  mutable
'''
