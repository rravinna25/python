'''
Write  a  program  to  print  first  20  odd  numbers

1) What  are  the  first  20  odd  numbers  ?  --->   1 , 3 , 5 , ....  39

2) What  is  printed  in  general ?  --->   2 * i  - 1  where  i  varies  from  1  to  20

3) Hint:  Do  not  use  range  object

4) Use  while  loop
'''
print('First  20  odd  numbers')
i = 1
while i <= 20:
	print(2 * i - 1)
	i += 1
