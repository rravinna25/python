'''
Write  a  program  to  determine  1.1 + 2.2 + 3.3 + .... n terms

1) sum =  0  + 1.1 * 1 + 1.1 * 2 + 1.1 * 3 + .......

2) What  is  added  to  sum  in  general ?  --->  1.1 * i   where  'i'  varies  from  1  to  n

3) Use  for  loop
'''
n = int(input('How  many  terms  would  you  like  to  add   :  '))  
sum = 0
for  i  in  range(1 , n + 1):  
	sum +=  1.1 * i  #  Adds  1.1 * i  to  sum  where  'i'  varies  from  1  to  n
print('Sum  :  ' ,  sum)
