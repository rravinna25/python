# Slice  demo  program (Home  work)
#        0      1         2          3         4         5        6        7
list = [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
#       -8     -7       -6        -5        -4       -3        -2      -1
print(list[2 : 7])  #list[2 : 7 :1]  --->  List  from  indexes   2  to  6  in  steps  of   1  i.e.  [3+4j,'Hyd' , True,None,10.8]
print(list[ : : ])  #list[0 : 8 :1]  --->  List  from  indexes   0  to  7  in  steps  of   1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[:])  #list[0 : 8 :1]  --->List  from  indexes   0  to  7  in  steps  of   1  i.e.  [25 , 10.8 , 3 + 4j , 'Hyd' , True , None , 10.8 , 'Hyd']
print(list[ : : -1]) #[-1:-9:-1]--->List  from  indexes   -1  to  -8  in  steps  of   -1  i.e.  ['Hyd , 10.8 , None , True , 'Hyd' , 3 + 4j , 10.8 , 25]
print(list[ : : 2]) #list[0 : 8 :2] --->List  from  indexes   0  to  7  in  steps  of   2  i.e.  [25, (3+4j), True, 10.8]
print(list[1 : : 2]) #list[1 : 8 :2]--->List  from  indexes   1  to  7 in  steps  of   2  i.e.  [10.8, 'Hyd', None, 'Hyd']
print(list[ : : -2]) #[-1:-9:-2]--->List  from  indexes   -1  to  -8  in  steps  of   -2 i.e['Hyd', None, 'Hyd', 10.8]
print(list[-2 : : -2]) #[-2:-9:-2]--->List  from  indexes   -2  to  -8  in  steps  of   -2 i.e[10.8, True, (3+4j), 25]
print(list[1 : 4]) #[1:4:1]--->List  from  indexes   1  to  3  in  steps  of   1  i.e[10.8, (3+4j), 'Hyd']
print(list[-4 : -1])#[-4:-9:-1]--->List  from  indexes   -4  to  -8  in  steps  of   -1 i.e[True, 'Hyd', (3+4j), 10.8, 25]
print(list[3 : -3])   #  list[3 : -3 :1]  --->  List  from  indexes   3  to  -4  in  steps  of   1  i.e.  ['Hyd' , True]
print(list[2 : -5])  #  list[2 : -5 :1]--->  List  from  indexes   2 to -6 in steps of 1 i.e [3 + 4j]
print(list[-1:-5]) #  list[-1 : -5 :1]--->  List  from  indexes -1 to -6 in steps of 1 i.e []


'''
1) How  to  obtain  list  with  first  two  elements ?  --->  list[ : 2]
    How  to  obtain  list  with  first  three  elements ?  --->  list[ : 3]
    How  to  obtain  list  with  first  'n'  elements ?  --->  list[ : n]

2) How  to  obtain  list  with  last  two  elements ?  --->  list[-2:]
    How  to  obtain  list  with  last  three  elements ?  --->  list[-3:]
    How  to  obtain  list  with  last  'n'  elements ?  --->  list[-n:]

3) How  to  obtain  list  without  first  two  elements ?  --->   list[2:]
    How  to  obtain  list  without  first  three  elements ?  --->   list[3:]
    How  to  obtain  list  without  first  'n'  elements ?  --->   list[n:]

4) How  to  obtain  reverse  list ?  --->  list[::-1]
'''
