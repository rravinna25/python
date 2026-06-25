'''
(Home  work)
Repeat   previous  program  with  comprehension

Input :  hyd  is  green  city

Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
a = input('Enter  any  sentence :  ')
b = a . split()
c = [[x . upper() , len(x)]  for  x  in  b]
print(c)


'''
c = [x . upper() , len(x)  for  x  in  b]
Is  the  statement  valid ?  --->  No  becoz  list  comprehension  can  not  have  multiple  expressions 
'''
