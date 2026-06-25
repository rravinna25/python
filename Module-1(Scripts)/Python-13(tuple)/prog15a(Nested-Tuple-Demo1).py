#  Nested   tuple  (Home  work)
a = ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(a) # ( (10 , 20)  ,  (30 , 40 , 50)  ,  (60 , 70 , 80 , 90) )
print(type(a)) # <class 'tuple'>
print(len(a)) #  Number  of  inner  tuples  in  tuple  'a'  i.e. 3
print(a[0]) #  1st  inner  tuple  (10,20)
print(a[1]) #   2nd  inner  tuple  (30,40,50)
print(a[2]) #  3rd  inner  tuple  (60,70,80,90)
print(a[0][1]) #  (10 , 20)[1]  is  20
print(a[1][2]) # (30 , 40 , 50)[2]  is  50
print(a[2][3]) # (60 , 70 , 80 , 90)[3]  is  90



'''
1) What  is  a  nested  tuple ?  --->  A  tuple  inside  another  tuple

2) Is  ((10 , 20 , 30))  a  nested  tuple ?  ---> No  becoz  comma  is   missing  and  it  is  treated  as
																	  a  single  tuple  of  three  elements

3) Is  (())  a  nested  tuple ?  --->  No  becoz  comma  is   missing  and  it  is  treated  as  empty  tuple
'''
