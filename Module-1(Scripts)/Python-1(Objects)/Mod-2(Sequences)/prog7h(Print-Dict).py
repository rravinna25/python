# How  to  print  dictionary  in  different  ways
a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Dictionary  with  print  function')
print(a) #  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print('Keys  of  dictionary')
for  x   in  a . keys():  #   'x'  is  each  element  of  the  list  in  dict_keys  object
    print(x)  # 10  <next  line>  20  <next  line>  15  <next  line>  18 <next  line>
print('Values  of  dictionary')
for  x   in  a . values(): #   'x'  is  each  element  of  the  list  in  dict_values   object
    print(x)   #  Ramesh  <next  line>  Kiran  <next  line>  Amar  <next  line>   Sita  <next  line>
print('All  the  tuples  of  dict_items   object')
for   x  in  a . items():  #   'x'  is  each  tuple    of  the  list  in  dict_items  object
	print(x)  #  (10 , 'Ramesh')  <next  line>  (20 , 'Kiran')  <next  line>  (15 , 'Amar')  <next  line>  (18 , 'Sita')  <next  line>
print('Elements  of  each   tuple')
for  x , y  in  a . items():  #   'x'   and  'y'  are  elements  of  each  tuple  in  the  list  of  dict_items  object
		print(x , y , sep = '...')   #  10  ...  Ramesh  <next  line>  20  ...  Kiran  <next  line>  15  ... Amar  <next  line>  18   ... Sita  <next  line>
print('Keys  and  values  of  dictionary')
for   x  in a . keys():   #   'x'  is  each  element  of  the  list  in  dict_keys  object
	print(x , a[x] , sep = ':')   #  10  :  Ramesh  <next  line>  20  :  Kiran  <next  line>  15 :  Amar  <next  line>  18 :  Sita  <next  line>



'''
1) for  x  in  dictionary:
	       print(x)
    Is  the  for  loop  valid ?  ---> Yes  becoz  keys()  method  is  executed   by  default

2) for  x  in  dictionary:
	       print(x)
     How  is  the  for  loop  interpreted ?  --->  for  x  in  dictionary . keys()
     																                     print(x)

3) dictionary = {'10' : 'A' ,  '20' : 'B' , '15' : 'C' , '18' : 'D'}
    for  x , y  in  dictionary . keys():
			 print(x , y)
     Is  the  for  loop  valid  ?  --->  Yes
	 What  are  'x'  and  'y'  in  1st  iteration  of  loop ?  --->   '1'  and  '0'
	 What  are  'x'  and  'y'  in  2nd  iteration  of  loop ?  --->   '2'  and  '0'
	 What  are  'x'  and  'y'  in  3rd  iteration  of  loop ?  --->   '1'  and  '5'
	 What  are  'x'  and  'y'  in  last  iteration  of  loop ?  --->   '1'  and  '8'

4) dictionary = {10 : 'A' ,  20 : 'B' , 15 : 'C' , 18 : 'D'}
    for  x , y  in  dictionary . keys():
			 print(x , y)
    Is  the  for  loop  valid  ?  --->  No

5) dictionary = {10 : 'ABC' ,  20 : 'DEF' , 15 : 'GHI' , 18 : 'JKL'}
    for  x , y , z   in  dictionary . values():
			 print(x , y , z)
     What  are  'x'  , 'y'  and  'z'  in  1st  iteration  of  loop ?  --->  'A' ,  'B'  and  'C'   respectively
     What  are  'x'  , 'y'  and  'z'  in  2nd  iteration  of  loop ?  --->  'D' ,  'E'  and  'F'  respectively
     What  are  'x'  , 'y'  and  'z'  in  3rd  iteration  of  loop ?  --->  'G' ,  'H'  and  'I'  respectively
     What  are  'x'  , 'y'  and  'z'  in  last  iteration  of  loop ?  --->  'J' ,  'K'  and  'L'  respectively

6) dictionary = {10 : 'AB' ,  20 : 'CDE' , 15 : 'FGHI'}
    for  x , y    in  dictionary . values():
			 print(x , y)
     What  are  'x'   and   'y'  in  1st  iteration  of  loop ?  --->  'A'   and  'B'  respectively
     What  are  'x'   and   'y'  in  2nd  iteration  of  loop ?  --->  Error  due  to  3  characters  in  'CDE'

7) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . keys():
	     print(x)
    Iteration         x
    -------------------------
        1                   10
        2                  20
        3                  15
        4                  18

8) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . values():
	        print(x)
    Iteration     x
    -----------------------
         1             'Ramesh'
         2             'Kiran'
         3             'Amar'
         4             'Sita'

9) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
    for  x   in  a . items():
	        print(x)
    Iteration         x
  ------------------------------------
           1              (10 , 'Ramesh')
           2              (20 , 'Kiran')
           3              (15 , 'Amar')
           4              (18 , 'Sita')

10) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
      for  x , y  in   a . items():
	       print(x , y , sep = ':')
     Iteration      x        y
    -----------------------------
          1               10        'Ramesh'
          2              20       'Kiran'
          3              15       'Amar'
          4              18       'Sita'

11) for  x , y  in   a . items():
	       print(x , y , sep = ':')
	 What  is  the  alternative  to  the  for  loop ? --->  for   x  in  a . items():
																							  print(x[0] , x[1] , sep = ':')
     What  are  x[0]  and  x[1]  ?  ---> x[0]  is  first  element  and  x[1]  is  2nd  element  of  each  tuple

     What  is  another  alternative  to  the  for  loop ? ---> for   x  in  a . items():
																							      print(*x , sep = ':')
     What  is  the  difference  between  x  and  *x  ?  --->  'x'  is  each  tuple  of  the  list  in  dict_items  object  and
	 																					   *x  is  elements  of  each  tuple  after  unpack

12) a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
     for  x  in  a . keys():
	       print(x , a[x])
    Iteration         x       a[x]
    -----------------------------------
         1                 10        'Ramesh'
         2                20        'Kiran'
         3                15        'Amar'
         4                18        'Sita'
'''
