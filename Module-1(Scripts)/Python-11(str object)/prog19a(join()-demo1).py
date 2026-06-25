#  join()   method  demo  program
a = ['15' , 'Aug' , '1947']
print('-' . join(a))   #  Joins  elements  of  list  'a'  with  '-'  to  form   '15-Aug-1947'
print('' . join(a))   #  Joins  elements  of  list  'a'  with  ''  to  form   '15Aug1947'
print(' ' . join(a))   #  Joins  elements  of  list  'a'  with  ' '  to  form   '15 Aug 1947'
#print(a . join(':')) #  Error :  No  join()  method  in  list  class  as  'a'  is  list
#print(join(a))  #  Error :  No  join()   function  in  current  module


'''
join()  method
-----------------
1) What  does  join()  method  do ?  --->  Joins  a  sequence  of  strings  with  the  delimeter  to  form  a  new  string

2) What  is  the  argument  of  join()  method ?  ---> Sequence  of  strings

3) What  does  join()  method  return ?  --->  The  joined  String

*4) In  other  words,  join()  method  converts  sequence  of  strings  to  a  string

5) Finally  join()  method  converts  list / tuple / set  to  a   string

6) a = (15 , 'Aug' , 1947)
    Is  '/' . join(a)  valid ?  --->  No  becoz  15  and  1947  are  not  strings  in  tuple  'a'

7) What  is  the  difference  between  split()  and  join()  methods ?  --->
														split()  method  converts  string  to  a   list  of  strings but
														join()  method  converts  a  sequence  of  strings  to  a  string

8) In  other  words,  split()  and  join()  are  quite  opposite  methods

Note:
1) 'Hyd' . method()
    Where  is  the  method  searched  and  why ?  --->  In  str  class  becoz  method  is  called  wrt  string

2) [10 , 20 , 30] . method()
    Where  is  the  method  searched  and  why ?  --->  In  list  class  becoz  method  is  called  wrt  list
	
3) (10 , 20 , 30) . method()
    Where  is  the  method  searched  and  why ?  --->  In  tuple  class  becoz  method  is  called  wrt  tuple
	
4) {10 , 20 , 30} . method()
    Where  is  the  method  searched  and  why ?  --->  In  set  class  becoz  method  is  called  wrt  set
	
5) {10 : 20 , 30 : 40} . method()
    Where  is  the  method  searched  and  why ?  --->  In  dict  class  becoz  method  is  called  wrt  dictionary
	
6) function()
    Where  is  the  function  searched  and  why ?  --->  In  current  module  becoz  it  is  not  called  wrt  any  object	
'''
