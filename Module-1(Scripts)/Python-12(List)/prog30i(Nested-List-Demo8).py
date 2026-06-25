#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a)  #  [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]] 
b = a . copy()  #   All  the  references  in  list  'a'  are  copied  to  list  'b'
a[0][1] = 25   #  Modifying  inner  lists  thru  list  'a'  is  as  good  as  modifying  list  'b'
a[1][2] = 55
a[2][3] = 95
print(b)  #  [[10 , 25] , [30 , 40 , 55] , [60 , 70 , 80 , 95]] 



'''
1) b = a . copy()
   What  are  copied  from  list  'a'  to  'b' ?  --->  References  of  inner  lists

2) If  inner  lists  are  modified  thru  list  'a' ,  are  changes  reflected  to  list  'b'  ?  --->
																									Yes  becoz  lists  'a'  and  'b'  share  same  inner  lists
'''
