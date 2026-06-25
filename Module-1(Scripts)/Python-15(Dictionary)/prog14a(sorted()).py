# sorted()  function  (Home  work)
a = {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}
b = sorted(a . keys())  #  Sorts  keys  of  dict  'a'  to  form  a  list  
print(b) # [5 , 10 , 15 , 18 , 20]
c = sorted(a . values())  #  Sorts  values  of  dict  'a'  to  form  a  list  
print(c) # ['Blue' , 'Green' , 'Red' , 'White' , 'Yellow']
d = sorted(a . items())  #  Sorts  tuples  on  first  element  to  form  a  list  
print(d) # [(5 , 'White') , (10 , 'Red') , (15 , 'Blue') , (18 , 'Yellow') , (20, 'Green')]
f  = sorted(a  , reverse = True)  #  Sorts  keys  of  dict  'a'  in  descending  to  form  a  list  
print(f) # [20 , 18 , 15 , 10 , 5]
print(a) # {10 : 'Red' , 20 : 'Green' , 15 : 'Blue' , 18 : 'Yellow' , 5 : 'White'}


'''
1) sorted(a . keys())  is  same  as  what ?  --->  sorted(a)

2) sorted(string) , sorted(list) ,  sorted(tuple) , sorted(set) ,  sorted(dict)
    sorted()  function  always  returns  list  irrespective  of  argument
'''
