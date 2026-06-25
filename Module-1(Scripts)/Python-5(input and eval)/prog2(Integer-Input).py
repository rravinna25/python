# How  to  read  an  integer  input ?  --->   int(input())
try:
	x = int(input('Enter  any  integer  number   :  '))  #  Read  string  input  which  is  converted  to  integer
	print(type(x))  #  <class   'int'>
	print(x)  #  User  input
except:  #   Executed  when  try  suite  raises  an  error
	print('Input  should  be  integer')


'''
Input     What  does  input()  read      What  does  int(input())  return
---------------------------------------------------------------------------------------
  25							  '25'                               int('25')  is  25
  10.8						  '10.8'                             int('10.8')  raises  error
  True						  'True'                            int('True')  raises  error
  Ten							  'Ten'                              int('Ten')   raises  error
  3 + 4j						  '3+4j'                             int('3+4j')  raises  error
------------------------------------------------------------------------------------------
1) What  is  the  result  of  int(10.8)  ?  --->  10
    What  is   the  result  of  int('10.8')  ?  ---> Error  due  to  string  float

2) What  is  the  result  of  int(True) ?  ---> 1
    What  is  the  result  of  int('True') ?  --->	Error  due  to  string  boolean

3) except:
	     stmt1
	     stmt2
	     stmt3
    Is  the  above  except  valid ?  ---> No  becoz  except  is  not  permitted  without  try

4) try:
	     stmt1
	     stmt2
	     stmt3
   Is  the  above  try  valid  ?  ---> No  becoz  try  is  not  permitted  without  except

5) In  other  words,  try  and  except  form  a  pair

6) try:
    stmt1
    except:
    stmt2
    Is  the  above  code  valid ?  --->  No  becoz  spacebar (or) tab  is  needed  before  stmt1  and  stmt2  due  to
									                    colon  after  try  and  except

7) In  other  words,  at  least   one  space  bar  (or)  tab  is  mandatory  at  the  begining  of  next  line  due  to  :

8) What  is  the  advantage  of  try  and   except  suites ? --->  Does  not  report  Error  and  prints  user  friendly  msg 
'''
