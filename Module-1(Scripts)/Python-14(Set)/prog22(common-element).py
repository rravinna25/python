'''
Write  a  program  to   obtain  common  elements  between  two  lists  using  sets

1) Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60]  and  2nd  list  be  [30 , 40 , 70 , 80 , 20]
    What  is  the  output ?  --->  [20 , 30 , 40]

2) Both  input  and  output  are  lists
'''
a = eval(input('Enter  1st  list  :  '))  #  Reads   1st   list
b = eval(input('Enter  2nd  list  :  '))   #  Reads   2nd   list
c = set(a)  #  Converts  1st  list  to  set
d = c . intersection(b)  #  Common  elements  between  set  and  list
e = list(d)  #   Converts  set  to  list
print('Common  elements  between  the  2  lists :  ' ,  e)


'''
1) b = [30 , 40 , 70 , 80 , 20]
    c = {10 , 20 , 30 , 40 , 50 , 60}
    Is  b . intersection(c)  valid ?  ---> No  becoz  list  does  not have  intersection()  method  

2) b = [30 , 40 , 70 , 80 , 20]
    c = {10 , 20 , 30 , 40 , 50 , 60}
	Is  c & b  valid ?  ---> No  becoz  'b'  is  not  a  set
'''
