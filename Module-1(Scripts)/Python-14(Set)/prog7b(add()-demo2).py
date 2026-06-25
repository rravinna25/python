# Find  outputs  (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
tpl = (10 , 20 , 30)
print(a) # {25 , 10.8 , 'Hyd' , True} in any order
print(id(a)) # Address of  set
a . add(tpl) #  Inserts  tuple  any  where  in  the  set
a . add('Sec')  #  Inserts  'Sec'  any  where  in  the  set
print(a) # {25 , 10.8 , 'Hyd' , True , (10 , 20 , 30) , 'Sec'} in  any  order
print(id(a)) # Same address
print(len(a)) # 6
#a . add([100 , 200 , 300]) # Error :  add()  method  expects  immutable  object  but   list  is  mutable
#a . add(set())  # Error :  add()  method  expects  immutable  object  but   set  is  mutable
#a . add({ })  # Error :  add()  method  expects  immutable  object  but   dict  is  mutable
