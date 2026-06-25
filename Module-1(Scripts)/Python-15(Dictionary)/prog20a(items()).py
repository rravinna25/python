#  items()  method  demo  program
a = {10 : 'Hyd' , 20 : 'Sec' , 15 : 'Cyb' , 18 : 'Pune'}
b = a . items()   #  Converts  dict  to  dict_items  object
print(b) # dict_items([(10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (18 , 'Pune')])
print(type(b)) # <class 'dict_items'>
for  x   in   b:  # 'x'  is  each  tuple  of  the  list  in  dict_items  object
        print(x) # (10 , 'Hyd') <next  line> (20 , 'Sec') <next line> (15 , 'Cyb') <next  line> (18 , 'Pune') <next line>
for  x , y   in  b:   #  x  and  y  are  elements  of  each  tuple  in  the  list  of  dict_items  object
        print(x , y , sep = ' ... ') # 10 ... Hyd <next line> 20 ... Sec <next line> 15 ... Cyb <next line> 18 ... Pune <next line>


'''
1) What  does  items()  method  do  --->  Returns  dict_items  object  which  has  list  of  tuples

2) What  are  the  two  elements  of  each  tuple ?  --->  (key , value)

3) for  x  in  dict . items():
	         pass
	Which  object  is  iterated  by  1st  for  loop ?  ---> The  list  in  dict_items  object

4) for  x , y  in  dict . items():
	           pass
    Which  object  is  iterated  by  2nd  for  loop ?  --->  The  list  in  dict_items  object
'''
