# Write  a  program  to  determine  mode  using  max()  function
list = [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
print('Mode  :  ' , max(list , key = list . count))  #  15 : Element  with  largest  count


'''
1) list = [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
   What  does  max(list)  do ?  ---> Returns  largest  element  of  the  list  i.e.  20

2) list = [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  does  max(list , key = list . count)  do ?  ---> Returns  element  with  largest  count  i.e.  15
																					10  -  4
																					20  - 3
																					15  -  5
																					18  -  2
																					12  -  1

3) max(list , keys = list . count)
     Is  the  statement  valid ?  --->  No  becoz  max()  function  does  not  have  keys   argument 

4) list = [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  does  min(list)  do ? --->  Returns  smallest  element  of  the  list  i.e.  10

5) list = [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  does  min(list , key = list . count)  do ?  --->  Returns  element  with  smallest  count  i.e.  12
																					10  -  4
																					20  - 3
																					15  -  5
																					18  -  2
																					12  -  1
'''
