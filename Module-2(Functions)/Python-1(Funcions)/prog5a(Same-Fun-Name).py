# Find  outputs
def  f1():  #  Deleted  :  Another  function  is  defined  with  same  name
	print('1st  function')
def  f1(): #  Deleted  :  Another  function  is  defined  with  same  name
	print('2nd  function')
def  f1():   #  Alive  :  Last  function
	print('3rd  function')
f1()  #  Executes  the  last  funciton  i.e.  3rd  function



'''
1) Can  multiple  functions  have  same  name ?  --->  Yes

2) Which  function  is  executed  when  multiple  functions  have  got  same  name ?  --->  The  last  function

3) What  about  remaining  functions  ?  --->  Deleted
'''
