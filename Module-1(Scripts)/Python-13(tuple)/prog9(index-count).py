 #index()  and  count()  methods  demo  program   (Home  work)
a = (10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25)
#     0    1      2     3    4     5     6    7     8    9    10
try:
	i = a . index(15)  #  Index  of   first  15  in  tuple  'a'  i.e.  2
	while  True:
		print('15 is found at index : ' , i) # Index  of  each  15  in  tuple  'a'
		i = a . index(15 , i + 1) #  Index  of  next  15  in  tuple  'a'
except:
		print(F'15  is  found  {a . count(15)}  times') #  Number of  times  15  is  found

'''
15 is found at index :  2
15 is found at index :  5
15 is found at index :  8
15  is  found  3  times
'''