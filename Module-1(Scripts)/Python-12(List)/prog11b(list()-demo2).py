#  Find  outputs (Home  work)
a = range(4 , 10 , 2)  #  Object  contains  elements  from  4  to  9  in  steps  of  2
b = list(a)  #  Converts  range  object  to  list
print(b) # [4 , 6 , 8]
print(type(b)) # <class 'list'>
a = list('Vamsi')  #   Converts  string  to  list
print(a) # ['V','a','m','s','i']
a = list() #  Returns  an  empty  list
print(a) #[]
#print(list(25)) # Error :  Argument  should   be  a  sequence  but  25  is  not  a  sequence
#print(list(10.8)) # Error :  Argument  should   be  a  sequence  but  10.8  is  not  a  sequence
#print(list(True)) # Error :  Argument  should   be  a  sequence  but  True  is  not  a  sequence
#print(list(None))  # Error :  Argument  should   be  a  sequence  but   None  is  not  a  sequence


'''
list()  function
-----------------
1) What  does  list(sequence)  do ?  --->  Converts  sequence  to  list  and  returns  list

2) What  does  list(no-args)  do ?  --->  Returns  an  empty  list

3) What  does  list(non-sequence)  do ?  --->   Raises  error
'''
