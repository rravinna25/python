# Write  a  program  to  create  a  list  with  1 ^ 2 , 2 ^ 2 , 3 ^ 2 , .....10 ^ 2  with  comprehension
a = [x **  2   for  x  in   range(1 , 11)]  #  Appends  x ^ 2  to  the list  where  'x'  varies  from  1  to 10
print(a)  #  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(type(a))  #  <class 'list'>
