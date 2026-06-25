# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) #   'a'  is  25  ,  'b'  is   () , 'c'  is  {}
print() #  Nothing
f1('Hyd' , 10 , 20 , 30) #   'a'  is   'Hyd'   ,  'b'  is   (10 , 20 , 30) , 'c'  is  {}
print() #  Nothing
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0) #  'a'  is  10.8  ,  'b'  is   (25 , 'Hyd' , True )  ,  'c'  is   {'EmpNo' : 12 , 'EmpName' : 'Rama  Rao' , 'Salary' : 10000.0}


'''
25
Hyd
(10, 20, 30)
10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}


1) def    f1(a , *b , **c):
	     pass
    What  is  the  difference  between  a , b  and  c ?  --->  'a'  is  regular  argument , 
																						    'b'  is  var-arg  positional  argument  due  to  single  *  and  
																						    'c'  is  var-arg  keyword  argument  due  to  **

2) if():
	     print('Hello')
    What  is  the  output ?  --->  Nothing  becoz  empty  tuple  is  false

3) if (10 , 20 , 30):
	     print('Hello')
    What  is  the  output ?  --->  Hello  becoz  non-empty  tuple  is  true

4) if{ }:
	    print('Hello')
    What  is  the  output ?  --->  Nothing  becoz  empty  dictionary  is  false

5) if {10 : 20 , 30 : 40}:
	     print('Hello')
    What  is  the  output ?  --->  Hello  becoz  non-empty  dictionary  is  true
'''
