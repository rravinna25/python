#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]  # Creates  a  list  of  5  elements
print(l) # [0 , 1 , 4 , 9 , 16]
print(type(l)) # <class 'list'>

s = {x * x   for   x   in   range(5)}   # Creates  a  set  of  5  elements
print(s) # {0 , 1 , 4 , 9 , 16}  in  any order
print(type(s)) # <class 'set'>

d = {x : x * x    for   x   in   range(5)}  # Creates  a  dictionary  of  5  key : value  pairs 
print(d) #{0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16}
print(type(d)) # <class 'dict'>

g = (x * x   for   x   in   range(5)) #   Creates  an  empty  generator  object
print(g) # __str__() method   returns  type  and  address  of  the  generator  object  'g'
print(type(g)) # <class  'generator'>


'''
1) a = [x * x   for   x  in  range(5)]
   What  is  the  statement  called ?  --->  List  comprehension  due  to  []

2) a = {x * x   for   x  in  range(5)}
    What  is  the  statement  called ?  ---> Set  comprehension  due  to  { }

3) a  = {x :  x * x   for  x  in  range(5)}
    What  is  the  statement  called ?  ---> Dictionary  comprehension  due  to  x : x * x

4) a = (x * x   for   x  in  range(5))
    What  is  the  statement  called ?  ---> Generator  expression  but  not  tuple  comprehension

4) a = [x * x   for   x  in  range(5)]
    What  does  the  statement  do ?  --->  Creates  a  list  of  five  elements  i.e.  [0 , 1 , 4 , 9 , 16]

5) a = {x * x   for   x  in  range(5)}
    What  does  the  statement  do ?  ---> Creates  a  set  of  five  elements  i.e.  {0 , 1 , 4 , 9 , 16}  in  any  order

6) a = {x : x * x   for   x  in  range(5)}
    What  does  the  statement  do ?  ---> Creates  a  dictionary  of  five  key : value  pairs  i.e.  {0 : 0 , 1 : 1 , 2 : 4 , 3 : 9 , 4 : 16}

7) a = (x * x   for   x    in  range(5))
    What  does  the  statement  do ?  ---> Creates  an  empty  generator  object  but  does  not  store
																 5  elements  in  the  generator
'''
