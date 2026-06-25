# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a : 10  <tab>  b  :  20  <tab>  c  :  30  <tab>  d  :  40  <tab> e  :  50 <tab>  f  :  60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error :  Function  f1()  expects  PA's  for  'a'  and  'b'  but  b = 2  is  a  keyword argument
#f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error :  Function  f1()  expects  KA's  for  'e'  and  'f'  but  5  is  a   positional  argument
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error :  Positional argument   40  is  not  permitted  after keyword argument  c = 30
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a : 10  <tab>  b  :  20  <tab>  c  :  30  <tab>  d  :  40  <tab> e  :  50 <tab>  f  :  60



'''
def  f1(a , b , / , c , d , * , e  , f):
	      pass
1) What  can  be  passed  for  'a'  and  'b' ?  --->  Positional  only  arguments  becoz  they  are  before  /

2) What  can  be  passed  for  'e'  and  'f' ?  --->  Keyword  only  arguments  becoz  they  are  after  *

3) What  can  be  passed  for  'c'  and  'd' ?  ---> Either  positional  arguments  (or)  keyword  arguments  becoz
				                                                              they  are  not  before  /  nor  after  *
'''
