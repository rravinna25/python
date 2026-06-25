# How  to  call  function  f1()  of  prog7a  with  from  statement ?
from   prog7a  import  f1  as   f2  #   Imports  function  f1()  of  prog7a  with  another  name  f2
def   f1():
	print('Function  of  prog7c')
f2()  #   Executes  function  f1()   of  prog7a
f1()  #    Executes  function  f1()   of  current  program
#prog7a . f1()  #  Error :  prog7a  is  not  imported


'''
1) from   prog7a  import  f1  as  f2
    What  does  the  statement  do ? --->  Imports  function  f1  from  module  prog7a  with  a  new  name  f2

2) What  is  this  process  called ?  --->  Function  alias

3) from   prog7a  import  f1
    What  is  the  issue  without  member  alias ?  --->																	
												Imported  function  f1()  is  deleted  becoz  another  function  is  defined  with  same  name

4) from   prog7a  import  f1()
    Is  the  statement  valid  ?  --->  No  due  to  ()
	
5) What  is  another  way  to  call  function  f1()  without  function  alias ?  --->	  Call  imported  function  f1()  before 
																														      another  function  is  defined  with  same  name
'''
