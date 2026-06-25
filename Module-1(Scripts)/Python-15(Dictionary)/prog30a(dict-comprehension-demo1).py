#  Find  outputs (Home  work)
d = {x : x ** 3   for    x   in  range(5)}   #  Appends  x : x ^ 3  to  dict  'a'
print(d) # {0 : 0 , 1 : 1 , 2 : 8 , 3 : 27 , 4 : 64}
print(type(d)) # <class 'dict'>


'''
Iteration   x     x ** 3    x  :  x ** 3      d
--------------------------------------------------------------------
       1		   0          0           0 : 0              {0 : 0}
       2		   1           1            1 : 1              {0 : 0 , 1 : 1}
       3		   2          8            2 : 8             {0 : 0 , 1 : 1 , 2 : 8}
       4		   3          27          3 : 27           {0 : 0 , 1 : 1 , 2 : 8 , 3 : 27}
       5		   4          64          4 : 64           {0 : 0 , 1 : 1 , 2 : 8 , 3 : 27 , 4 : 64}

1) {x ** 3  for  x  in  range(5)}
    What  is   the  statement  called  ? ---> Set  comprehension  due  to  { }

2) [x ** 3  for  x  in  range(5)]
    What  is   the  statement  called  ? ---> List  comprehension  due  to  []

3) {x : x ** 3  for  x  in  range(5)}
    What  is   the  statement  called  ? ---> Dictionary  comprehension  due  to  x : x ** 3 and  { }

4) (x ** 3  for  x  in  range(5))
    What  is   the  statement  called  ? --->  Generator  expression  but  not  tuple  comprehension
	
5) (x ** 3  for  x  in  range(5))
    Why  python  does  not  have  tuple  comprehension ?  --->  Since  tuple  is  immutable 
																												and  
																								 hence  x ^ 3  can  not  be  appended  to  the  tuple
'''
