#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]  #  Nested  list
print('Nested list  with  print function')
print(a) #  [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Each  inner  list   of   outer  list  without  indexes')
for  x  in  a:  # 'x'  is  each  inner  list  of  list  'a'
    print(x)  #  #  [10 , 20]   <next  line>  [30 , 40 ,  50]   <next  line>  [60 , 70 , 80 , 90]  <next  line>
print('Elements  in  the  form   of  matrix   without  using  indexes')
for  x  in  a: # 'x'  is  each  inner  list  of  list  'a'
    for  y  in  x:   #  'y'  is  each  element  of  inner  list  'x'
        print(y , end =' ')
    print() #  Move  to  next  line
print('Elements  in  the  form   of  matrix  using  indexes')
for  i  in  range(len(a)):
    for j in  range(len(a[i])):
        print(a[i][j] , end = ' ')
    print()


'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90


1st  for  loop
----------------
Iteration      x
-----------------------
      1             [10 , 20]
      2             [30 , 40 , 50]
      3             [60 , 70 , 80 , 90]


2nd  for  loop
------------------
    x                                 y
----------------------------------
    [10 , 20]                    10
                                     20
    [30 , 40 , 50]            30
    						        40
    						        50
    [60 , 70 , 80 , 90]     60
    						        70
    						        80
    						        90

3rd   for  loop
------------------
    i       j           a[i][j]
   ------------------------------
    0     0              10
           1              20
    1     0              30
           1		       40
    	   2		       50
    2     0		       60
           1		       70
           2		       80
           3		       90
'''
