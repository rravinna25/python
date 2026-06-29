# calc . py
__all__ =  ['add' , 'x'  , 'mul' , 'c1']
x = 100
y = 200
def  add(a , b):
	return   a + b
def	  sub(a , b):
	return   a - b
def	  mul(a , b):
	return   a * b
def	  div(a  ,  b):
	return  a / b
class   c1:
	def  m1(self):
		print('m1  method')


'''
__all__
----------
1) What  is   __all__ ?  --->  List  of  those  members  of  the  module  which  are  imported  when  *  is  used

2) from  calc   import   *
    Which  members  are  imported ?  --->  Those  members  which  are  in  __all__  list  of  cal  module

3) What  happens  when  __all__  list  has  an  invalid  member ?  --->  from  module  import  *  raises  ImportError

4) Where  is  __all__  list  defined  ?  --->  Inside  the  module  i.e.  Any  where  in  the  module

5) from  calc   import   *
    Which  members  are  imported  when  cal  module  does  not  have  __all__  list ?  --->
									All  the  members  are  imported  becoz  default  __all__  is   every  member  of  the  module

6) from  calc   import   *
    Which  members  are  imported  when  __all__  list  is  empty  in  cal  module ?  --->  No  member  is  imported

7) from  calc  import   y , sub , mul
    Which  members  are  imported ? --->  y , sub  and  mul  and  ignores  __all__  list  becoz  *  is  not  used

8) __all__  list  is  used  only  when  from  statement  has  *

9) import  module
    Which  members  are  imported ?  ---> No  member  is  imported  becoz  import  statement  imports  module  but  not  members
'''
