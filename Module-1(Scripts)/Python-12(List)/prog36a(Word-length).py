'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''
a = input('Enter  any  sentence :  ')  #  Reads  a  string  to  object  'a'
b = a . split()  #   Divides  string  into   list  of  stings  based  on  white  space  delim
c = []
for  x  in  b:  #  'x'  is  each  string  of  list  'b'
	c . append([x . upper() , len(x)])  #  Appends  list  of  2  elements  to  list  'c'
print(c)


'''
Let  input  be  'hyd is green city'
What  is  list  'b' ?  --->  ['hyd ', 'is' , 'green' , 'city']

        x           x . upper()     len(x)     [x . upper() , len(x)]       list  c
-------------------------------------------------------------------------------------------------
                                                                                               []
       'hyd'         'HYD'           3         ['Hyd' , 3]                       [['HYD' , 3]]
       'is'            'IS'              2         ['IS' , 2]                         [['HYD' , 3] , ['IS' , 2]]
       'green'     'GREEN'       5         ['GREEN' , 5]                  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5]]
       'city'        'CITY'          4         ['CITY' , 4]                     [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]


1) c . append(x . upper() , len(x))
    Is  the  statement  valid ?  --->  No  becoz  append()  method  expects  single  argument  but  not  two  arguments

2) c . append((x . upper() , len(x)))
    What  does  the  statement  do  ?  --->  Appends  tuple  of  two  elements  to  list  'c'
    What  does  print(c)  do ?  --->  Prints  list  of  tuples

3) c . append( {x . upper() , len(x)})
    What  does  the  statement  do  ?  --->  Appends  set  of  two  elements  to  list  'c'
    What  does  print(c)  do ?  --->  Prints  list  of  sets

4) c . append( {x . upper() : len(x)} )
    What  does  the  statement  do  ?  ---> Appends  dictionary  to  list  'c'
    What  does  print(c)  do ?  ---> Prints  list  of  dictionaries
	
5) c = ()
    c . append(['Hyd' , 3])
	Is  the  statement  valid ?  --->  No  becoz  tuple  does  not  have  append()  method
'''
