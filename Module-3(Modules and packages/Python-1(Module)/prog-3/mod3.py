# Find  outputs
x = 30
def   disp():
	print('disp  function  of  same  module')
class   c1:
	def   m1(self):
		print('m1  method  of  class  c1  in  same  module')
from  mod1   import  *  #  Imports  object  'x' , function  f1()  and  class  c1  of  mod1
from  mod2   import  *  #  Imports  object  'x' , function  f1()  and  class  c1  of  mod2
print(x)  #  20 : Object  'x'  of  mod2 
disp() #  Executes  disp()  function  of  mod2
a = c1() #  Creates  mod2 . c1  class  object
a . m1()  #  Executes  method  of  mod2 . c1  class


'''
1) Where  does  ref  'x'  initially  points ?  --->  To  object  30
    Where  does  ref  'x'  points  after  1st  from  statement  is  executed ?  --->  Object  10  
	What  about  object  30 ?  --->  Gets  deleted  as  it  does  not  have  reference
    Where  does  ref  'x'  points  after  2nd  from  statement  is  executed ?  --->  Object  20
	What  about  object  10 ?  --->  Gets  deleted  as  it  does  not  have  reference

2) print(x)
    What  is  printed ?  --->  Object  'x'  of  mod2  i.e.  20

3) Where  does  ref  disp  initially  points ?  --->  Function  of  current  module
    Where  does  ref  disp  points  after  1st  from  statement  is  executed ?  --->  Function  of  mod1
	What  about  function  of  current  module ?  --->  Gets  deleted  as  it  does  not  have  reference
	Where  does  ref  disp  points  after  2nd  from  statement  is  executed ?  --->  Function  of  mod2
	What  about  function  of  mod1 ?  --->  Gets  deleted  as  it  does  not  have  reference

4) disp()
     Which  function  is  executed ?  --->  Function  of  mod2

5) Where  does  ref  c1  initially  points ?  --->  class  of  current  module
     Where  does  ref  c1  points  after  1st  from  statement  is  executed ?  ---> class  of  mod1
	 What  about  class  of  current  module ?  --->  Gets  deleted  as  it  does  not  have  reference
	 Where  does  ref  c1  points  after  2nd  from  statement  is  executed ?  ---> class  of  mod2
	 What  about  class  of  mod1 ?  --->  Gets  deleted  as  it  does  not  have  reference
																			   
6) a = c1()
    Which  class  object  is  created  ?  ---> class  of  mod2

*7) Finally,  members  of  last  imported  module  are  used
'''
