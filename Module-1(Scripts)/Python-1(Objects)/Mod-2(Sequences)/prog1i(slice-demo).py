# Find  outputs
a = 'Sankar Dayal Sarma'
print(a[7 : 12]) #  a[7 : 12 : 1]  --->  string from indexes 7 to 11 in steps of 1 i.e. Dayal
print(a[7 : ]) # a[7:18:1] ----> string from index 7 to 17 insteps of 1 i.e.Dayal Sarma
print(a[ : 6]) # a[0:6:1] ---> string from index 0 to 5 in step of 1 i.e. Sankar
print(a[ : ]) #a[0:18:1] ---> string from index 0 to 17 instep of 1 i.e. Sankar  Dayal  Sarma
print(a[:  : ])  #  a[0 : 18 : 1]  --->  string  from  indexes  0  to  17   in  steps  of   1  i.e.  Sankar  Dayal  Sarma
print(a[1 : 10 : 2]) #a[1:10:2] ---> string from indexes 1 to 9 in steps of 2 i.e.akrDy
print(a[0 : : 2]) #a[0:18:2] ---> string from indexes 0 to 17 in steps of 2 i.e.Sna<space>aa<space>am
print(a[1 : : 2]) #a[1:18:2] ---> string from indexes 1 to 17 in steps of 2 i.e. akrDylSra
print(a[-5 : -1]) #a[-5:-1:1] ---> string from indexes -5 to  -2   insteps of 1 i.e.Sarm
print(a[::-1])  #  a[-1 : -19 : -1]  --->  string  from  indexes  -1  to   -18   in  steps  of   -1  i.e.  Reverse  string
print(a[-1:-5:-1]) #string from indexes -1 to -4 in steps of -1 i.e. amra
print(a[ : : -2]) #a[-1:-19:-2]--->string from indexes -1 to -18 in steps of -2 i.e. arSlyDrka
print(a[3 : -3])  #  a[3 : -3 : 1]  --->  string  from  indexes  3  to  -4  in  steps  of   1  i.e.  kar<space>Dayal<space>Sa
print(a[2 : -5]) #a[2:-5:1] --->string from indexes 2 to -6 in steps of 1 i.e. nkar<space>Dayal<space>
print(a[-1:-5]) #a[-1:-5:1]--->string from indexes -1 to  -6 in steps of 1 i.e.  Empty string
print(a[3 : 3]) #a[3:3:1]--->string from indexes 3 to 2 in steps of 1 i.e.  Empty string


#   0      1      2      3      4      5     6         7       8       9    10    11     12         13     14     15      16     17
#   S      a      n      k      a       r                D       a       y      a      l                  S       a       r       m       a
#  -18   -17  -16   -15  -14    -13  -12       -11     -10    -9    -8    -7    -6          -5      -4      -3      -2     -1



'''
1) How  to  obtain  first  two  characters  of  the  string ?  --->  string[ : 2]
    How  to  obtain  first  three  characters  of  the  string ?  ---> string[ : 3]
    How  to  obtain  first  'n'  characters  of  the  string ?  ---> string[ : n]

2) How  to  obtain  last  two  characters  of  the  string ?  --->  string[-2 : ]
    How  to  obtain  last  three  characters  of  the  string ?  ---> string[-3 : ]
    How  to  obtain  last  'n'  characters  of  the  string ?  ---> string[-n : ]

3) How  to  obtain  whole  string   without  first  two  characters ?  --->  sting[2 : ]
    How  to  obtain  whole  string   without  first  three  characters ?  ---> string[3 : ]
    How  to  obtain  whole  string   without  first  'n'  characters ?  ---> 	string[n : ]

4) How  to  obtain  reverse  string ?  --->  string[::-1]
'''
