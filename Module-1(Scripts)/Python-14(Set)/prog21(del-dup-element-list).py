'''
Write  a  program  to  remove  duplicate  elements  of   list  using  set

1) Let  input  be  [False , 25 , 10.8 , 1  , 25 , 0 , 'Hyd' ,  10.8 , 1.0 , None , 'Sec' , 'Hyd' , True  ]
    What  is  the  output ?  --->	[False , 25 , 10.8 , 1 , 'Hyd' , None , 'Sec']

2) Both  input  and  output  are  lists
'''
a = eval(input('Enter  list  with  duplicates :  '))  #  Reads  a  list
b = set(a)  #  Converts   list  to  set  so  that  duplicate  elements  are  removed
c = list(b)  #   Converts  set  to  list
print('List  without  duplicates :  ' ,  c)  # Prints  list
