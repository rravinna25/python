#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:  #  'x'  is  each  inner  list   of  list   'a'
	print(x) # [10 , 20] <next line> [30 , 40 , 50] <next line> [60 , 70 , 80 , 90]  <next line>
print()	
'''
for  x , y  in  a:
	print(x , y ,	sep = '...') # 10...20 <next line> Error :  Excess  elements  in  2nd   inner  list
'''
for  x , *y  in  a:
	print(x , y ,	sep = '...') # 10...[20] <next line>  30 ... [40 , 50]  <next line>   60  ... [70 , 80 , 90]  <next line> 



'''
2nd  inner  list  has  got  three  elements  but  2nd  for  loop  has  only  two  variables  and  hence  2nd  iteration  raises  an  error
'''
