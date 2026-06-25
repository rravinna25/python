'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
try:
	a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
	i = -1
	while  i := a . index(15 , i + 1):   #   Index  of   each  15  in  list  'a'  until   15  is  not  found
		print(i)  #   Index  of  each  15  in  list  'a'  i.e.  2 <next  line>  5 <next  line>  8 <next  line>
except:
	print(F'15  is  found  {a . count(15)}  times ') # 15  is  found  3  times
