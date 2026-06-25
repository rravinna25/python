'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
list = eval(input('Enter list:')) #  Reads  list
new = [] #  Empty  list
while  list:  # Repeat until  list  is  empty
	small = min(list)  #   Smallest   element  of  the  list
	new . append(small)  #  Appends  smallest  element  of  the  list  to  a  new  list
	list. remove(small)  #   Removes  smallest  element  of  the  list
print('Sorted  list : ' , new) #  Sorted  list
