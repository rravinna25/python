'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''
a = [x **  2  for  x  in  range(1 , 21)  if  x ** 2 % 2 == 0]  #  Appends  x ^  2  to  list   if  x ^ 2  is  divisible  by  2  where  'x'  varies  from  1  to  20
print('Squares  of  1  to  20  which  are  divisible  by   2 :  '  , a)  #  [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]


'''
x     x **  2 %  2 ==   0      List  'a'
-------------------------------------------
1                False                    []
2                True                    [4]
3                False                   [4]
4                True                   [4 , 16]
5                False                   [4 , 16]
....
20              True                   [4 , 16 , 36 , ....  400]
'''
