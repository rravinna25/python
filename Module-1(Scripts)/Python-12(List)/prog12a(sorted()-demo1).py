# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)  #  Sorts  elements  of  list  'a'  and  returns  a  new  list  of  sorted  elements
print(b) # [5 , 10 , 12 , 15,  20]
print(type(b)) # <class  'list'>
c = sorted(a , reverse = True) #  Sorts  elements  of  list  'a'  in  descending  order  and  returns  a  new  list  of  sorted  elements
print(c) # [20 , 15 , 12 , 10 , 5]
print(a) # Original  list  i.e. [10 , 20 , 15 , 5 , 12]


'''
sorted()  function
---------------------
1) What  does  sorted(list)  do  ?  --->  Sorts  elements  of  the  list  in  ascending  order

2) Where  are  the  results  stored  ?  --->  In  another  list

3) Is  argument  list  modified ?  --->  No  and  it  remains  unchanged

4) How  to  sort  list  in  descending  order ?  --->  sorted(list , reverse = True)
'''
