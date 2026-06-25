'''
Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

1) Let  input  be  PYTHON
    What  is  the  output ?  ---> PYON

2) Let  input  be  Hyd
    What  is  the  output ?  --->  Nothing
'''
a = input('Enter  any  string : ')  #  PYTHON
b = ''
if len(a) >=  4:
	b = a[:2] + a[-2:]
print('Result : ' , b)


'''
1) What  does  a[:2]  do ?   --->   Extracts  first  two  characters  of  the  string 

2) What  does  a[-2:]  do ?   --->  Extracts  last  two  characters  of  the  string 
'''
