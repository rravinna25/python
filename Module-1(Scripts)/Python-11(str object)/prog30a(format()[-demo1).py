# format()  method  demo  program
empno = 25
ename = 'Rama  Rao'
sal = 10000.9274
print('Emp  Number  :  {}  \t  Emp  Name  :  {}  \t  Salary  :  {}' . format(empno , ename , sal))  #  Emp  Number  :  25  <tab>  Emp  Name  :  Rama Rao  <tab> Salary  :  10000.9274
print('Emp  Number  :  {}  \t  Emp  Name  :  {}  \t  Salary  :  {:.2f}  ' . format(empno , ename , sal))  #  Emp  Number  :  25  <tab>  Emp  Name  :  Rama Rao  <tab> Salary  :  10000.93
print('Emp  Number  :   \t  Emp  Name  :  \t  Salary  :  ' . format(empno , ename , sal))  #  Emp  Number  :  <tab>  Emp  Name  :   <tab>  Salary  :
print('{} \t  {}  \t  {} \t' . format(empno , ename , sal))  #  25  <tab>  Rama  Rao  <tab>  10000.9274
print('' . format(empno , ename , sal))  #  Empty  string
#print('{} \t  {}  \t  {} \t{}' . format(empno , ename , sal))  #   Error :  Excess  {}  in  the  string
print('{} \t  {}   ' . format(empno , ename , sal)) #   25  <tab>  Rama  Rao


'''
format()  method
---------------------
1) What  does  format(args)  do ?  --->  
											Concatenates  all  the  arguments  of  format()  method  to  form  a  string  and  returns  string

2) What  is  the  syntax  of  format()  method ?  --->  string . format(arguments)  

3) What  is  the  constraint  for  format()  method ?  --->  String  should  have  { }

4) What  is  the  role  of  { }  in  the  string ?  --->  Placeholder

5) Every  { }   in  the  string  is  replaced  with  what ?  --->  The  argument  value

6) How  many  braces  can  be  in  the  string ?  --->  Number  of  arguments

7) What  happens  when  there  are  excess  braces  in  the  string ?  --->  format()  method  raises  error
    
8)	What  happens  when  there  are  no  braces  in  the  string ?  --->  Arguments  are  not  concatenated
																															and  
																											  the  same  string  is  returned

9) What  happens  when  there  are  few  braces  in  the  string ?  --->  Excess  arguments  are  not  concatenated

10) What  does  format()  method  return ?  --->  Concatenated  String

11) What  does  {:.2f}  indicate  ?  --->   Two  digits  after  decimal  point  for  float  number

12) What  is  the  similarity  between  F  string   and  format()  method ?  --->
																						They  concatenate  object(s)  (or)  arguments  to  form  a  string

13) 'Emp  Number  :  {}  \t  Emp  Name  :  {}  \t  Salary  :  {}' . format(empno , ename , sal)
      How  to  replace  format()  method   with  F  string ?  ---> 
																		F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :  {sal}'

14) What  is  recommended  between  them  ?  --->  F  string

Note:
1) format()  method  was  used  before  python  3.6  becoz  there  was  no  F  string

2) F  string  is  an  enhancement  to  format()  method  from  python  3.6
'''
