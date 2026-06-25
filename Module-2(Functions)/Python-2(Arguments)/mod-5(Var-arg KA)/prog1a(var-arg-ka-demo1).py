# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #   Dictionary  of  2  key : value   pairs is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)    #   Dictionary  of  3  key : value   pairs is  passed  to  the  function
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')   #   Dictionary  of  4  key : value   pairs is  passed  to  the  function
disp()   #   Empty  Dictionary   is  passed  to  the  function


'''
Results
<class   'dict'>
{'RollNo' : 10 ,  'StudName' : 'Rama  Rao'}
<Blank  line>
Results
<class   'dict'>
{'EmpNo' : 25 , 'EmpName' : 'Sita' , 'Salary' : 10000.0}
<Blanck line>
Results
<class   'dict'>
{'AcNo' : 30 , 'CustName' : 'Kiran' , 'Balance' : 20000.0 , 'Gender' : 'm'}
<Blanck line>
Results
<class 'dict'>
{}
<blanck line>
'''

'''
1) def   disp(**a):
	      pass
    disp(10 , 20 , 30)
    Is  the  function  call  valid ?  --->  No  becoz  positional  arguments  can  not  be  passed  to  the  function  as
											               **  indicates  var-arg  keyword  args

2) def   disp(**a):
	      pass
    disp(RollNo : 25 , StudName : 'Sita')
    Is  the  function  call  valid ?  --->  No  becoz  delimeter  should  be  =  in  keyword  arg  but  not  :

3) def   disp(**a):
	      pass
    disp('EmpNo' = 25 , 'EmpName' = 'Sita' , 'Salary' = 10000.0)
    Is  the  function  call  valid ?  --->  No  becoz  argument  name  can  not  be  in  quotes

4) def   disp(**a):
	      pass
    disp(Emp No = 25 , Emp Name = 'Sita' , Salary = 10000.0)
    Is  the  function  call  valid ?  ---> No  becoz  space  is  not  permitted  in  the  argument  name  as  it  is  a  special  character

5) def   disp(**a):
	      pass
     disp(Emp_No = 25 , Emp_Name = 'Sita' , Salary = 10000.0)
     Is  the  function  call  valid ?  --->  Yes  becoz  _  is  permitted  in  argument  name

6) def   disp(**a):
	      pass
    disp(Emp-No = 25 , Emp-Name = 'Sita' , Salary = 10000.0)
    Is  the  function  call  valid ?  --->  No  becoz  '-'  is  not  permitted  in  the  argument  name  as  it  is  a  special  character

7) def   disp(**a):
	      pass
    d = {'x' : 10 , 'y' : 20}
    disp(d)
    Is  the  function  call  valid ?  --->  No  becoz  positional  argument  can  not  be  passed  to  the  function  due  to  presence  of  **

8) def   disp(**a):
	      pass
    d = {'x' : 10 , 'y' : 20}
    disp(d = d)
    Is  the  function  call  valid ?  --->  Valid   due  to  keyword  argument
'''
