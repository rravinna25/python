# Find  outputs  (Home  work)
class   c1:
	def  __del__(self):
		print('destructor')
		return  25
a = c1()  #  Creates  an  empty  c1  class  object
print(a . __del__()) #  Executes  destructor  which  returns  25  i.e.  print(25)
print('Hello')
del   a  #  Executes  destructor  before  object  'a'  is  deleted  and  25  gets  ignored


'''
destructor
25
Hello
destructor



1) print(del   a)
    Is  the  statement  valid ?  --->  No  becoz  del  operator  can  not  be  used  in  print()  function  as 
												       del  operator  does  not  return  any  result

2) a . __del__()
    Is  object  'a'  lost  after  execution  of  destructor ?  --->  No  becoz  destructor  is  called  explicitly
'''
