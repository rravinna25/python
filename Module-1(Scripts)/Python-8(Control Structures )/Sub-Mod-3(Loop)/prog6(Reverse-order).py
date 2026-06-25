#  How  to  print  list  elements  in  reverse  order   without  slice
a = [25 , 10.8 , 'Hyd' , True]
print('Indexed for loop')
for  i  in  range(1 , len(a) + 1):  
	print(a[-i])  #  Prints  a[-i]  where  'i'  varies  from  1  to  len
#How   to  print  each  element  of  list  in  reverse  order  with  for  each  loop  (Do  not  use  2nd  variable  and  slice)  --->  Not  possible
	

# for ... each  loop  can  iterate  thru  the  sequence  from  left  to  right  but  not  from right  to  left  (i.e.  reverse  order)
