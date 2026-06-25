# Find  outputs  (Home  work)
def  f1():
	return   10 , 20 , 30 #   Returns  a  tuple  of  3  elements
# End  of  the  function
x = f1()  #  Function  returns  (10,20,30)  which  is  assgined  to  'x'
print(x) #  (10 , 20 , 30)
print(type(x))   #  <class  'tuple'>
a , b , c =  f1()   #  Function  returns  (10,20,30)  which  is  unpacked  to  objects  a , b  and  c
print(a)  # 10
print(b) #  20
print(c) #   30
print('for  loop')
for  k   in   f1():   #  Function  returns  (10,20,30)  which  is  iterated  with  for  loop
	print(k)  #  10  <next  line>  20   <next  line>  30   <next  line>


'''
(10,20,30)
<class 'tuple'>
10
20
30
for loop
10
20
30


How  many  times  is  f1()  function  executed  in  the  program ?  --->  Thrice  becoz  it  is  called  3  times
'''
