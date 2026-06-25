# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():  #  'x'  is  each  element  of  the  list  in  dict_keys  object
	print(x , end = '\t') #  10  <tab>  30  <tab>  50  <tab>
print()  #  Moves  to  next  line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():  #  'x'  is  each  element  of  the  list  in  dict_values  object
	print(x , end = '\t') # 20  <tab>   40  <tab>  60  <tab>
print()  #  Moves  to  next  line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():  #  'x'  is  each  tuple  of  the  list  in  dict_items  object
	print(x , end = '\t') #  (10,20)  <tab>  (30,40)   <tab>   (50,60)   <tab>
print()  #  Moves  to  next  line
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:  #  'x'  is  each  element  of  the  list  in  dict_keys  object
		print(x , end = '\t') #  10  <tab>  30  <tab>  50  <tab>
print()  #  Moves  to  next  line		


'''
1) What  does  keys()  method  do ?  --->  Returns  dict_keys  object  which  has  list  of  all  the  keys  of  dictionary

2) What  does  values()  method  do ?  --->  Returns  dict_values  object  which  has  list  of  all  the  values  of  dictionary

3) What  does  items()  method  do ?  --->  Returns  dict_items  object  which  has  list  of  tuples  where  each  tuple
																    has  2  elements  i.e.  (key , value)

4) for  x  in  dict:
	       print(x)
    Which  method  is  called  by  the  above  for  loop  ?  --->  keys()  method  by  default
'''
