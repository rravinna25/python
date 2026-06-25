# values()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . values()  #  Converts  dict  to  dict_values  object
print(b) # dict_values(['Hyd' , 'Sec' , 'Cyb' , 'Pune'])
print(type(b)) # <class 'dict_values'>
for  x   in   b:  #  'x'  is   each  element  of  the  list  in   dict_values  object
	print(x) # Hyd <next line> Sec <next line> Cyb <next line> Pune <next line>


'''
1) What  does  values()  method  do  --->  Returns  dict_values  object  which  has  list  of  all  the  dictionary  values

2) for  x  in  dict . values():
	        pass
	Which  object  is  iterated  by  for  loop ?  --->  The  list  in  dict_values  object
'''
