# add()  method  demo  program  (Home  work)
a = set()  #  Empty  set
a . add(True) #  Inserts  True  into   empty  set
a . add(25) #  Inserts  25  anywhere  in  the  set
a . add(10.8)  #  Inserts  10.8  anywhere  in  the  set
a . add(1) # Ignores  1  as True is already  in the set
a . add('Hyd') #  Inserts  'Hyd'   anywhere  in  the  set
a . add(25) # Ignores  25  as 25 is already  in the set
a . add(None) #  Inserts   None   anywhere  in  the  set
a . add('Hyd') # Ignores  'Hyd'   as 'Hyd' is  already  in the set
a . add(1.0)  # Ignores  1.0   as True is already  in the set
print(a) # {True,25,10.8,'Hyd',None} in  any  order
#a . add(10 , 20 , 30) # Error :  add()  method  expects  single  argument  but  not  3  arguments
#a . add([10 , 20 , 30]) # Error :  add()  method  expects  immutable  object  but   list  is  mutable


'''
add()   method
-----------------
1) What  does  add(x)  do ?  --->  Inserts   'x'  any  where  in  the  set  becoz  set  is  unordered

2) How  many  arguments  can  add()  method  take ?  --->  Single

3) Is  set . add(mutable-object)  valid ? --->  No  becoz  set  can  not  hold  mutable  element

4) In  other  words,  argument  of  add()  method  should  be  immutable  object  only

5) What  does  set . add(sequence)  do  ?  --->  Inserts  sequence  any  where  in  the  set  but  not  elements  of  sequence
												                          (Like  append()  method  of  list  class)
'''
