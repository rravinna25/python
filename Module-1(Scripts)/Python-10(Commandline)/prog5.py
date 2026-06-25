'''
Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

1) py  prog5.py  10   20    15.8   5   12.6
    What  is  argv ?  --->  ['prog5.py' , '10' , '20' , '15.8' , '5' , '12.6']
    What  is  list  'a' ?  --->  [10 , 20 , 15.8 , 5 , 12.6]
    How  to  sort  list  'a' ?  ---> sorted(a)
    How  to  sort  list  'a'  in  descending  order  ?  ---> sorted(a , reverse = True)

2) py  prog5.py   25   'Ten'
    What  is  the  output ?  ---> Do  not  send  number  and  string  
	
3) py  prog5.py  
    What  is  the  output ?  --->  Pls  send  inputs
	
4) py  prog5.py    Hyd  'Sec'  'Cyb'
    What  are  the  outputs ?  --->   ['Cyb' , 'Hyd' , 'Sec']
													   ['Sec' , 'Hyd' , 'Cyb']
'''
from sys import argv
try:
	a = []  #  Empty  list
	for  x  in  argv[1:]:  #   'x'  is  each  command  line  input  of  argv  list
		a . append(eval(x)) #   Appends  each  command  line  input  to  list  'a'
	print('Ascending  order : ' , sorted(a)) #    List  'a'  in  ascending  order
	print('Descending  order : ' , sorted(a , reverse = True))  #  List  'a'  in  ascending  order
except  NameError:
	print('Input  string  should  be   in  single  (or)  triple  quotes')
except  TypeError:
	print('Do  not  send  number  and  string')


'''
1) py  prog5.py   'Hyd'   'Sec'   'Cyb'
   What  is  argv  list ?  --->  ["  'Hyd'  " , "  'Sec' " , "  'Cyb'  "]
   What  is  list  'a' ?  --->  ['Hyd' , 'Sec' , 'Cyb']
'''

#2) py  prog5.py  '''Hyd'''   '''Sec'''   '''Cyb'''
'''       What  is  argv  list ?  --->  ["  '''Hyd'''  " , "  '''Sec'''  " , "  '''Cyb'''  "]
		   What  is  list  'a' ?  --->  ['Hyd' , 'Sec' , 'Cyb']

3) py  prog5.py   "Hyd"   "Sec"   "Cyb"
    Which  statement  raises  an  error ?  ---> eval("Hyd")  returns  object  Hyd  which  does  not  exist

4) py  prog5.py   Hyd   Sec   Cyb
    Which  statement  raises  an  error ?  ---> eval('Hyd')  returns  object  Hyd  which  does  not  exist

5) py  prog5.py
    What  is  the  output  of  command ?  --->  []  twice

6) py  prog5.py  25   'Ten'
    Which  statement  raises  an  error ?  --->
													sorted([25 , 'Ten'])  raises  an  error  becoz  number  and  string  can  not  be  sorted
'''
