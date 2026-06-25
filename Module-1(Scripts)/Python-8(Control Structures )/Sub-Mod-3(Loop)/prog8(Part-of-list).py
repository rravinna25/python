#  How  to  print  list  elements  from  indexes  2  to  4  without  slice
a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']
print('Indexed for loop')
for   i  in  range(2 , 5):  #  Prints  a[i]  where  'i'  varies  from  2  to  4  
	print(a[i])  #  Hyd  <next  line>  True  <next  line>  3+4j  <next  line>
#How  to  print  elements  from  indexes  2  to  4  of  list  'a'  with  for  each  loop   without  using  2nd  variable  and  slice  --->  Not  possible


# for ... each  loop  can  iterate  thru  whole  sequence  but  not  a  part  of  the  sequence
