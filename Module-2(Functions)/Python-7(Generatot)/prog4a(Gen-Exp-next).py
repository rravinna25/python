#  How  to  define  generator  thru  expression
import  time
g = (x * x   for  x  in  range(5))   #   Creates  an  empty  generator   object
print(type(g))  #  <class  'generator'>
print(g)   #   __str__()  method  returns  type  and  address  of  object 'g'
while   True:
	try:
		print(next(g)) #   0 <next line>  1  <next line>  4  <next line>  9  <next line>  16 <next line>
		time . sleep(1)
		print('Hello')
	except   StopIteration:
		break
# End  of  while  loop
print('End')
#print(next(g))  #  StopItration  Error :  Object  'g'  does  not  have  7th  element


'''
<class 'generator'>
Type  and  address  of  object  'g'
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello
End


1) g = [x * x   for  x  in  range(5)]
    What  is  type(g) ?  ---> <class  'list'>

2) g = [x * x   for  x  in  range(5)]
    print(g)
	What  is  printed ?  ---> [0 , 1 , 4 , 9 , 16]

3) g = [x * x   for  x  in  range(5)]
    Is  next(g)  valid ?  --->  No  becoz  next()  function  expects  generator  but  list  is  passed
'''
