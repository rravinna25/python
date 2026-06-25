#  Find  outputs
import   time
a = [10 , 20]
print(a)  #  [10 , 20]
for  x  in  a:
	a . append(x)
	print(a)  #  [10 , 20 , 10]  <next  line>  [10 , 20 , 10 , 20]  <next  line>  [10 , 20 , 10 , 20 , 10]  <next  line>   [10 , 20 , 10 , 20 , 10 , 20]  <next  line>   and  so  on
	time . sleep(2)   #  Suspends  execution  for  2  sec