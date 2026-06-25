# startswith()  method  demo  program  (Home  work)
a = 'Hyderabad is green city'
print(a . startswith('Hyd'))  #  True  :  object  'a'  starts  with  'Hyd'
print(a . startswith('Sec'))  #  False  :  object  'a'  does  not  start  with  'Sec'
print(a . startswith('hyd')) #   False  :  object  'a'  does  not  start  with  'hyd'
print(a . startswith('green' , 13))  #  True   :  object  'a'  starts  with  'green'  from  index  13


'''
startswith()  method
-------------------------
1) What  does  str1 . startswith(str2)  do ?  --->  Returns  True  when  str1  starts  with  str2  and  False  otherwise

2) What  does  str1 . startswith(str2 , index)  do ?  --->  Returns  True  when  str1  starts  with  str2  from  the  specified
																					     index  and  False  otherwise

3) str1 . startswith(str2) 
    What  is  the  default  2nd  argument  ?  ---> 0
'''
