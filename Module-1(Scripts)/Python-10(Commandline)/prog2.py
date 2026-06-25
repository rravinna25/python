'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8   7  40    35.6
    What  is  the  largest  command  line  input ?  ---> 40
    What  is  argv ?  --->  ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?   ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  ---> '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->
													Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  ---> Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  largest  command  line  input ?  --->  'Vamsi'

4) py   prog2.py   25   'Ten'
    What  is  the  output ?  --->  Inputs  can  not  be  number  and  string

5) Hint1: Use  for  loop

6) Hint2: Use  try  and  except
'''
from sys import argv
try:
	a = []  #   Empty  list
	for  x  in  argv[1:]:  #   'x'  is  each   command  line  input  of   argv  list
		a . append(eval(x))  #   Appends  each  command  line  input  to  list  'a'
	print('Largest  input :  ' , max(a))  #  Largest  command  line  input
except  ValueError:
	print('Send  at  least  one  input')
except  NameError:
	print('Input  string  has  to  be  in  single  (or)  triple  quotes')
except  TypeError:
	print('Do  not  senf  number  and  string')



'''
1) py  prog2.py
    What  is  argv[1:] ?  ---> []
    Which  statements  raises  an  error ?  ---> max([ ])  raises  ValueError

2) py   prog2.py   'Hyd'  'Sec'  'Cyb'
    What  is  argv[1:] ?  ---> ["  'Hyd'  ", "  'Sec'  " , "  'Cyb'  "]

3) Same  thing  for  triple  quotes  also

4) py   prog2.py   Hyd  Sec  Cyb
    What  is  argv[1:] ?  ---> ['Hyd' , 'Sec' , 'Cyb']
    Which  statement  raises  an  error ?  ---> eval('Hyd')  returns   object  Hyd  which  does  not  exist

5) py   prog2.py   "Hyd"   "Sec"   "Cyb"
    What  is  argv[1:] ?  --->  ["Hyd" , "Sec" , "Cyb"]
    Which  statements  raises  an  error ?  --->  eval("Hyd")  returns   object  Hyd  which  does  not  exist

6) py   prog2.py   25   'Ten'
    What  is  argv[1:] ?  ---> ['25' , "  'Ten'  "]
    Which  statements  raises  an  error ?  --->  
															max([25 , 'Ten'])  raises  TypeError  becoz  number  and  string  can  not  be  compared

7) What  happens  when  error  is  raised ?  --->  Skips  rest  of  the  program  and  executes  except  suite  

8) What  is  the  advantage  of  handling  error ? --->  Does  not  report  error  
																								and
																					 prints  user  friendly  message 
'''
