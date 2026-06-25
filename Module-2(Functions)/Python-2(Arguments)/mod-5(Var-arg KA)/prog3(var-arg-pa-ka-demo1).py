# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))  #  <class 'tuple'>
	print(a) #  (25 , 10.8 , 'Hyd' , True)
def   f2(**a):
	print(type(a))  #  <class 'dict'>
	print(a)  # {'EmpNum' :25 , 'EmpName' :  'Sita' , 'Salary' : 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)  #  Tuple  of   4  elements  is  passed to  the   function
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)  #  Dictionary of   3  key :  value  pairs is  passed to  the   function


'''
<class 'tuple'>
(25, 10.8, 'Hyd', True)

<class 'dict'>
{'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
'''
