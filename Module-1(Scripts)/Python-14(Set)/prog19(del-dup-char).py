'''
(Home  work)
Write  a  program  to  remove  duplicate  characters  of  the  string  using  set

1) Let  input  be   Rama  Rao
    What  is  the  output  ? ---> Ram<space>o

2) Both  input  and  output  are  strings

3) How  to  convert  string  to  set  ?  --->  set(string)
    How  to  convert  set  to  string ?  ---> '' . join(set)

4) What  is  the  result  of  str({'H' , 'y' , 'd'})  ? --->  "{'H' , 'y' , 'd'}"  but  not  'Hyd'
'''
a = input('Enter  input  string :  ') #  Reads  a  string
b = set(a)  #  Converts string  to  set
c = '' . join(b)  #  Joins  elements  of  set 'b'  to  form a   string
print('String  without  duplicates  :  ' , c)
