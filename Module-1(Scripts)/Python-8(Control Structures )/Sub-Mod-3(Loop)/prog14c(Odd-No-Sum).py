'''
Write  a  program  to  determine  1 + 2 + 3 + .... + n  without  using  formula  n * (n + 1) / 2

What  is  added  to  sum  in  general ? --->  'i'  where  'i'  varies  from  1  to   n

Hint:  Use  for  loop
'''
sum = 0
for  i  in  range(1 , 21):  
	sum +=  2 * i - 1   #  Adds  2 * i -  1  to  sum  where  'i'  varies  from   1  to  20
print('Sum  of  first  20  odd  numbers :  ' , sum)
