# F   string  demo  program
x = 25
print(F'{x}')  # Converts  object  'x'  to  string  i.e.  '25'
print(F'x')  #   x  itself  :   Braces  are  missing  for  object  'x'
print('{x}')  #  {x}
print('x')  #   x
print(x)   #  25
print(F'x = {x}')  #  x = 25
print(F'{x =  }')  #  x = 25
print(F'x =') #  x =
print(F'x : {x}')  #  x : 25
print(F'{x:}')  #  25  and  ignores  :


'''
F  string
----------
1) What  does  F  string  do ?  --->  Converts  any  python  object  to  string

2) What  is  the  syntax  of  F  string ?  --->   F'{object}'

3) What  does  F'{object}'  do ?  --->  Converts  object  to  string

4) What  does  F  stands  for  --->  Format  string

5)  Is  f'{object}'  valid ?  --->  Yes  becoz  F  and  f  same  

6) What  does  F'{object=}'  do ?  --->  Returns   name  of  the  object  and   value  of  the  object  in  the  form  of  string 

7) F'{object=}'
    Can  any  other  delimeter  be  used  instead  of  = ?  ---> No  and  it  should  be  =  only

8) What  are  the   three  ways  to  convert  object  to  string ?  --->  str(object)  ,  '%s'  %object  ,  F'{object}'

9) What  is  the  difference  between  eval()  function  and  F  string ?  ---
																						eval()  function  converts  string  to  any  python  object  but
																						F '{object}'  converts  object  to string
'''
