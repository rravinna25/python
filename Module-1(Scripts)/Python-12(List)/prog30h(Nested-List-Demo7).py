#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x , y , *z in  a:
	print(x , y ,	z , sep = '...') #  10 ... 20 ... [] <next line> 30 ... 40 ... [50]  <next line> 60 ... 70 ... [80 , 90]  <next line>
print()	
for  x , *y , z in  a:
	print(x , y ,	z , sep = '...') #  10 ... [] ... 20  <next line> 30 ... [40] ... 50  <next line> 60 ... [70 , 80]  ... 90  <next line>
print()	
for  *x , y , z in  a:
	print(x , y ,	z , sep = '...') #  [] ... 10 ... 20  <next line> [30] ... 40 ... 50  <next line> [60 , 70] ... 80 ... 90  <next line>
'''
for  *x , y , *z in  a:  #   Error  due  to  multiple  *'s
	print(x , y ,	z , sep = '...') 
'''	
