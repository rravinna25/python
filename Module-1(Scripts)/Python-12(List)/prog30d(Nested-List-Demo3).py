#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:  #  'x'  is  each  inner  list   of  list   'a'
    print(x) # [10 , 20] <next line> [30 , 40] <next line> [50 , 60] <next line> [70 , 80]  <next line>
print()
for  x , y  in  a: #  'x'  and  'y'  are  elements  of  each  inner  list  of  list  'a'
	print(x , y , sep = '...') # 10 ... 20 <next line> 30 ... 40 <next line> 50 ... 60 <next line> 70 ... 80  <next line>
