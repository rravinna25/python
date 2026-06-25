# Find  outputs
def   f1(x ,  a  =  []):
	a . append(x)
	print('List  :  '  ,  a)
#End  of  the  function
print('__defaults__ : ' , f1 . __defaults__)   #  ([],)
f1(3)  #  'x'  is   3  ,  'a'  is   default  value   [] , result  is  [3]
print('__defaults__ : ' , f1 . __defaults__)  #   ([3],)
f1(5)   #  'x'  is   5  ,  'a'  is   default  value   [3] , result  is  [3 , 5]
print('__defaults__ : ' , f1 . __defaults__)  #   ([3 , 5],)
f1(6)    #  'x'  is   5  ,  'a'  is   default  value   [3 , 5] , result  is  [3 , 5 , 6]
print('__defaults__ : ' , f1 . __defaults__)  #   ([3 , 5 , 6],)
f1(10 , [20])   #  'x'  is   10  ,  'a'  is  [20] , result  is  [20 , 10]
print('__defaults__ : ' , f1 . __defaults__)   #   ([3 , 5 , 6],)



'''
1) When  is  __defaults__  modified ?  --->  As  soon  as  function  modifies  default  argument  

2) How  is  __defaults__  modified  when  default  argument  is  modified  ?  --->  Since  they  point  to  same  list

3) f1(10 , [20])
    Why  is  __defaults__  not  modified ?  ---> 
														Since  function  is  modifying   actual   parameter  list  but  not  default  argument

4) When  is  __defaults__  remains  unchanged  ?  --->  When  function  modifies  actual  parameter  list

5) What  is  the  use  of  __defaults__ ?   --->  Default  values  are  fetched  from  __defaults__
'''
