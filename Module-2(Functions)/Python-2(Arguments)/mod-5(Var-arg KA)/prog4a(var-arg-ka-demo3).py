#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0) # Emp  Number  :  25  <tab>  Emp  Name  :  Sita  <tab>  Salary  :	10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) # Error :  Function  is  expecting  arguments  empno , ename , sal  but  eno , empname , salary  are  passed
f2(empno = 25 , ename = 'Sita' , sal = 10000.0) # {'empno'  :  25  , 'ename'  :  Sita , 'sal'  : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0) # { 'eno' :  25 , 'empname'  :  Sita  , 'salary'  :	10000.0}
