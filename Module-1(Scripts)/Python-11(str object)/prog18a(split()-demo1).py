# split()  method demo program
a = '15-Aug-1947'
b = a . split('-')  #   Divides  string  into  list  of  strings  based  on   '-'  delimeter
print(b)   #  ['15' , 'Aug' , '1947']
print(type(b))  #  <classs  'list'>
for   x  in   b:  #  'x'  is  each  element  of  list  'b'
	print(x)   #  15  <next  line>  Aug  <next  line>  1947  <next  line>


'''
split()  method
------------------
1) What  does  split()  method  do ? --->  Divides  a  string  into  a  list  of  strings  based  on  delimeter

2) What  is  the  argument  of  split()  method ?  --->  Delimeter  string

3) What  does  split()  method  return ? ---> A  list  of  strings

4) Is  split(No-args)  valid  ? ---> Yes  and  default  delimeter  is  white  space

5) What  is  white  space ?  --->  ' ' , '\n'  , '\t'  and  '\r'

6) In  other  words,  split(No-args)  divides  string  based  on  four  delimeters

7) '15-Aug-1947' . split('-')
     What  does  the  method  do  ? --->  Divides  date  string  into  [date , month , year]
'''
