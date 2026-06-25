#  keys()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . keys()  #  Converts  dict  to  dict_keys  object
print(b) # dict_keys([10 , 20 , 15 , 18])
print(type(b)) # <class  'dict_keys'>
for  x  in   b:  #  'x'  is  each  element  of  the  list  in  dict_keys  object
        print(x) # 10 <next line> 20 <next line> 15 <next line> 18 <next line>


'''
1) What  does  keys()  method  do  --->  Returns  dict_keys  object  which  has  list  of  all  the  dictionary  keys

2) for  x  in  dict . keys():
			 pass
     Which  object  is  iterated  by  for  loop ?  --->  The  list  in  dict_keys  object
'''
