# How  to  read  complex  input ?  --->  complex(input())
try:
	x = complex(input('Enter  complex  number  :  '))  #  Reads  string  input  which  is  converted  to  complex
	print(type(x))  #  <class  'complex'>
	print(x)  #  User  input
except:    #  Executed  when  try  suite  raises  an  error
	print('Input  should  be  a  complex  number')


'''
Input       input() reads      complex(input())  returns
------------------------------------------------------------------------
3+4j           '3+4j'                complex('3+4j')  is  3+4j
25              '25'                   complex('25')  is   25+0j
4j               '4j'                   complex('4j')  is  4j
10.8            '10.8'                complex('10.8')  is  10.8 + 0j
True           'True'               complex('True')  raises  Error
Ten             'Ten'                complex('Ten')  raises  Error
3+j4            '3+j4'               complex('3+j4')  raises  error
3+4i             '3+4i'               complex('3+4i')  raises  error
4j+3             '4j+3'              complex('4j+3')  raises  error
----------------------------------------------------------------------------
1) What  is  the  result  of  complex(True) ?  --->  1 + 0j
    What  is  the  result  of  complex('True')  ---> Error

2) What  is  the  result  of  complex(4j + 3) ?  --->  3 + 4j
     What  is  the  result  of  complex('4j + 3') ? ---> Error
'''
