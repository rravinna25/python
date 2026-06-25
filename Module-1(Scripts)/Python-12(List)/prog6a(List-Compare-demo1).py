# Comparing  Lists
a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]  #  Ref  'b'  points  to  a  different  list  as  list  is  mutable  and  not  reusable
c = [10 , 20 , 25 , 9]
d = [10 , 20 , 7 , 22]
print(a == b) # True  :  Elements  of  lists 'a'  and  'b'  are  same
print(a  is   b) # False :  References   'a'  and  'b'  points  to  different lists
print(a < c) # True : 15 < 25
print(a > d) # True : 15 > 7
print(a >= c) #False : 15 is  not  >=  25
print(a <= d) #False : 15 is  not  <=  7
print(a != c) # True : 15 is  not  = 25
print(a != b) #False :  Same  elements  in  lists  'a'  and   'b'
print(a == c) #False :  15 is  not  = 25


'''
1) Can  lists  be  compared  with  > , < , ==  and  so  on ?  --->  Yes  only  in  python

2) What  are  compared  when  == , >  , < , >= , <=  and  !=  are  used  between  lists ?  --->  1st  non-matching  elements

3) What  does  list1 == list2  do ?  --->  Compares  objects   i.e.  lists
    What  does  list1  is  list2  do  ?  ---> Compares  references  i.e.  id's

4) Can  there  be  multiple  lists  with  same  elements ?  --->  Yes  becoz  list  is  mutable  and  not  reusable
'''
