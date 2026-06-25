# Tricky  program
# add()  and  remove()  methods  (Home  work)
a = set()  #   Empty  set
a . add(25) # Inserts   25 into  empty  set
a . add(10.8) #  Inserts  10.8  any  where in  the  set
a . add('Hyd')   #  Inserts  'Hyd'   any  where in  the  set
a . add(True)  #  Inserts  True   any  where in  the  set
a . add(None)  #  Inserts  None  any  where in  the  set
a . add('Hyd') #  Ignored :  set  already  contains  'Hyd'
a . add(1)  #  Ignored :  set  already  contains   True
print(a) # {25,10,8,'Hyd',True,None} in  any  order
print(len(a)) #   5
a . remove(25) # Removes 25 from  set
print(a)   #   {10,8,'Hyd',True,None}  (Order  is  same as  line  11)
#a . append(100) # Error :   No  append()  method  in  set
#a . add(set())  #   Error :  set  can  not  be  inserted  as   it  is  mutable
a . add(()) #  Inserts  ()   any  where   in  set  'a'
#a . add([])  #   Error :  List  can  not  be  inserted  as   it  is  mutable
print(a)  #  {10.8 , 'Hyd' , True , None , ()}  in  any  order
#a . add({})  #  Error :  dict  can  not  be  inserted  as   it  is  mutable



'''
1) Which  method  is  used  to  append  an  element  to  list  ?  --->  append()  method

2) Which  method  is  used  to  insert  an  element  into  set  ?  --->  add()  method

3) Which  method  is  used  to  remove  an  element  from  list  and  set  ?  --->  remove()  method
'''
