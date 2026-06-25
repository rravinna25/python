#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a = [x  for  x  in  range(1 , 21)  if  x % 2 == 0]   #  Appends  'x'  to  list  'a'  where  'x'   varies  from  1  to  20  in  steps  of  1  and  x  should  be  divisible  by  2
print('Even numbers  between  1  and  20 :  ' , a)  #   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''
x      x  % 2  ==  0    List   'a'
-------------------------------------
1            False              []
2            True              [2]
3            False             [2]
4            True              [2 , 4]
5            False             [2 , 4]
.....
20          True              [2 , 4 , 6 , .... , 20]
'''
