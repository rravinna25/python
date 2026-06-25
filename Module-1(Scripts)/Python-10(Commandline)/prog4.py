'''
Write  a  program  to  determine  average  of  command  line  inputs

1) py   prog4.py   10.8   25   True   14.6   19   False   7.4
    What  is  argv ?  --->['prog4.py' , '10.8' , '25' , 'True' , '14.6' , '19' , 'False' , '7.4']
    What  is  list  'a'  ?  ---> 	[10.8 , 25 , True , 14.6 , 19 , False , 7.4]
	How  to  determine  sum  of  list  elements ?  ---> sum(a)
    How  to  determine  number  of  list  elements ?  ---> len(a)

2) py   prog4.py
    What  is  the  output ?  ---> Pls  send  number  inputs

3) py   prog4.py  25   'Ten'
    What  is  the  output  ?  --->  Pls  send  number  inputs
'''
from sys import argv
try:
	a = []  #   Empty  list
	for  x  in  argv[1:]:  #  'x'  is  each  command  line  input  of  argv  list
		a . append(eval(x)) #  Appends  each  command  line  input  to  list  'a'
	print('Average  :   ' , sum(a) / len(a)) #   Average  of  command  line  inputs
except  ZeroDivisionError:
	print('Send  atleast  one  input')
except  NameError , TypeError:
	print('Do  not  send   number  and  string')


'''
1) py  prog4.py
    Which  statements  raises  an  error ?  --->  sum(a) / len(a)  raises  ZeroDivisionError  i.e.  0 / 0
    What  is  argv[1:] ?  ---> []
    What  is  sum([]) ?  ---> 0
    What  is  len([]) ?  ---> 0

2) py   prog4.py   25   Ten
    Which  statements  raises  an  error ?  --->  eval('Ten')  returns   object  Ten   which  does  not  exist

3) py   prog4.py   25   'Ten'
    Which  statements  raises  an  error ?  ---> sum([25 , 'Ten'])  raises  TypeError  becoz  number  and  string  can  not  be  added

4) import   sys
    Is  print(argv)  valid ? ---> No  becoz  argv  can  not  be  used  as  it  is  not  imported
    How  to  use  argv ?  ---> sys . argv

5) from  sys  import  argv
     Is  print(sys . argv)  valid ?  ---> No  becoz  sys  can  not  be  used  as  it  is  not  imported
     How  to  use  argv ?  --->  argv
'''
