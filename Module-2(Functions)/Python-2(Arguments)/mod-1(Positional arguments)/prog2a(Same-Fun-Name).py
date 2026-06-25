# Find  outputs (Home  work)
def  f1():   # Deleted :  Another  function  is   defined  with same  name  f1
	print('No-argument  function')
def  f1(x):   # Deleted :  Another  function  is   defined  with same  name  f1
	print('Single  argument  function  : ' , x)
def  f1(x , y):   # Deleted :  Another  function  is   defined  with same  name  f1
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):  #  Recognized :  Last  function
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30) # Three argument function:  <space>  10 <space> 20 <space> 30
#f1(40 , 50) # Error : Function  f1()  is  expecting  3  arguments  but   not  two  arguments
#f1(60) # Error : Function  f1()  is  expecting  3  arguments  but   not  one  argument
#f1() # Error : Function  f1()  is  expecting  3  arguments  but   not  zero  arguments


'''
1) Which  function  is  executed  when  functions  have  same  name ?  --->  The  last  function

2) What  about  remaining  functions ?  --->  Dead

3) When  is  a  function  dead ?  --->   When  another  function  is  defined  with  same  name

4) Python  does  not  have  function  overloading (unlike  c++)

5) What  is  function  overloading ?  --->  Same  function  does  multiple  operations

6) Each  python  function  can  do  only  one  operation
'''
