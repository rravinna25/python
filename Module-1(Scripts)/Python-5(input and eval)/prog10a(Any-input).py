# What  is  the  advantage  of  eval(input()) ?  --->  It  can  read  any  kind  of  input
try:
	x = eval(input('Enter  any  input  :  '))
	print(type(x))
	print(x)
except:
	print('Input  string  should  be  in  quotes')


'''
Input                             input() reads                     eval(input())  returns
--------------------------------------------------------------------------------------
  25                                      '25'                             eval('25')  is   25
  10.8                                    '10.8'                          eval('10.8')  is  10.8
  3+4j                                   '3+4j'                          eval('3+4j')  is  3+4j
  False                                  'False'                         eval('False')  is  False
  None                                  'None'                         eval('None')  is  None
  Hyd                                    'Hyd'                          eval('Hyd')  is  object   Hyd
  'Hyd'                                  "  'Hyd'  "                   eval("  'Hyd'  ")   is   'Hyd'
  [25 , 10.8 , 'Hyd']               "[25 , 10.8 , 'Hyd']"     eval("[25 , 10.8 , 'Hyd']")  is   [25 , 10.8 , 'Hyd']
---------------------------------------------------------------------------------------------
1) What  is  the  advantage  of  eval(input()) ?  --->  It  can  read  any  type  of  input
    What  is  the  dis-advantage  of  eval(input()) ?  ---> String  input  has  to  be  in  quotes

2) What  does  int(input())  do  ?  --->  Reads  only  integer  input
    What  does  float(input())  do ?  ---> Reads  either  float  input  (or)  integer  input
    What  does  complex(input())  do ?  ---> Reads  only  complex  input

3) Finally  eval(input())  can  be  used  as  an  alternative  to   int(input()) , float(input())  and  so  on

4) Which  function  is  ideal  to  read  employee  number ?   --->  int(input())   becoz  emp  number  is  usually  integer
    Which  function  is  ideal  to  read   employee  name ?  --->	input()  becoz  emp  name  is  a  string
    Which  function  is  ideal  to  read  salary ?   ---> float(input())  becoz  salary  is  float
    Which  function  is  ideal  to  read   gender ?  --->  	input()  becoz  gender  is  male  (or)  female  which  is  a  string
    Which  function  is  ideal  to  read   married ? --->  eval(input())  but  not  bool(input())

5) What  is  the  issue  with  eval(input())  for  reading  emp  number ?  --->  
																							Reads  even  non-int  input  but  does  not  report  any  error
    What  is  the  issue   with  eval(input())  for  reading  emp  name ?  ---> Emp  name  has  to  be  in  quotes
    What  is  the  issue   with  eval(input())  for  reading  salary ?  --->  
																							Reads  even  non-float  input  but  does  not  report  any  error
    What  is  the  issue   with  bool(input())  for  reading  married ?  ---> Reads  True  even  when  input  is  False
'''
