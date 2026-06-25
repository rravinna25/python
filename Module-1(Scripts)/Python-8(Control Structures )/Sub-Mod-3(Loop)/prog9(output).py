#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1  #  Increments  each  element  of  list
print('a :  ' , a)  #  [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1  #  Increments  variable  'x'  but  not  each  element  of  list
print('b :  ' ,  b) #   [10 , 20 , 15 , 18]


'''
1) for ... each  loop  can  iterate  thru  sequence  but  can  not  modify  elements  of  sequence.

2) In  other  words,  for  ...  each  loop  treates  list  as  read-only 
'''
