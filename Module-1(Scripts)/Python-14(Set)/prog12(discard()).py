# discard()  method  demo  program (Home  work)
a = {25 , 10.8 , 'Hyd' , True}
print(a) # {25 , 10.8 , 'Hyd' , True}  in  any  order
a . discard('Hyd')  # Removes 'Hyd' from  the  set
print(a) # {25 , 10.8  , True}  in  any  order
a . discard('Sec') #  No  error  even though  set  does  not  have  'Sec' 
print(a) # {25 , 10.8 , True}  in  any  order
#a . remove('Sec') # Error :   Set  does  not  have  'Sec' 


'''
discard()  method
---------------------
1) What  does  discard(x)  do ?  --->  Removes  'x'  from  the  set

2) What  does  discard(Invalid-element)  do ?  --->  Nothing

3) In  other  words,  discard(invalid-element)  does  not  raise  error  nor  deletion
'''
