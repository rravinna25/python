'''
Write  a  program  to  sort  string  in  alphabetical  order

Let  input  be  RAJESH
What  is  the  output ?  --->  AEHJRS
'''
a = input("Enter  any  string  :  ")
b = sorted(a)  #  Sorts  each  char  of  the  string  and  returns  a  list  of  sorted  chars
c = '' . join(b)  #  Joins  chars  of  list  'b'  with  ''  to  form  a  string
print('Sorted  string  :   ' ,  c)


'''
Let  input  be  'RAJESH'
1) What  is  object  'a'  ?  --->  RAJESH

2) What  is  list  b ?  --->   ['A' , 'E' , 'H' , 'J' , 'R' , 'S']

3) What  is  object  c ?  --->  AEHJRS

4) a = 'Hyd'
    Is  a . sorted()  valid ?  --->  No  becoz  str  class  does  not  have  sorted()  method 
'''
