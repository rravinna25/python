# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15) #  Removes  first  occurence  of  15  from  the  list
	print(list) #[10 , 20  , 18 , 15 , 12 , 15 , 19]
	list . remove(25)  #  Executes  except  suite  as  25  is  not  the  list
except:
	print('25  is   not  in  the  list') #  25  is   not  in  the  list


'''
remove()   method
---------------------
1) What  does  remove(x)  do ?  --->  Removes   first  occurance  of  'x'  from  the  list

2) What  does  remove()  method  do  if  'x'  is  not   in  the  list ?  --->  Throws  ValueError

3) How  to  remove  all  ocurances  of  'x'  from  the  list ?  --->   Call  remove()  method  in  a  loop
'''
