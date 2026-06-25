'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #  a[0 : 7 : 2]  --->  String  from  indexes  0  to  6  in  steps  of  2  i.e. Rm<space>a
print(a [ : 7])  #  a[0 : 7 : 1]  --->  String  from  indexes  0  to  6  in  steps  of  1  i.e. Rama<space>Ra
print(a [2 : 4])   #  a[2 : 4 : 1]  --->  String  from  indexes  2  to  3  in  steps  of  1  i.e. ma
print(a [2 : ])  #  a[2 : 8 : 1]  --->  String  from  indexes  2  to  7  in  steps  of  1  i.e. ma  Rao
print(a [ : 4 ]) #  a[0 : 4 : 1]  --->  String  from  indexes  0  to  3  in  steps  of  1  i.e. Rama
print(a [ : : 2])  #  a[0 : 8 : 2]  --->  String  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1])  #  a[-6 : -1 : 1]   --->  String  from  indexes  -6  to  -2  in  steps  of  1  i.e. ma<space>Ra
print(a [-6 : ])  #  a[-6 : 8 : 1]  --->  String  from  indexes   -6  to  7  in  steps  of  1  i.e. ma<space>Rao
print(a [: -4 : -1])  #  a[-1 : -4 : -1]   --->  String  from  indexes  -1  to  -3  in  steps  of  -1   i.e.  oaR
print(a [-3 : -1]) #  a[-3 : -1 : 1]  --->  String  from  indexes  -3  to  -2  in  steps  of  1  i.e.  Ra
print(a [-3 : ])  #  a[-3 : 8 : 1]  --->  String  from  indexes  -3  to  7  in  steps  of  1  i.e. Rao
print(a [ : : ])  #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e. Rama Rao
print(a [ : ]) #  a[0 : 8 : 1]  --->  String  from  indexes  0  to  7  in  steps  of  1  i.e. Rama Rao
print(a [ : : -1])  # a[-1 : -9 : -1]  --->  String  from  indexes  -1  to  -8  in  steps  of  -1  i.e.  oaR<space>amaR
print(a [ : : -2]) #  a[-1 : -9 : -2]  --->  String  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])  #  a[-2 : -9 : -2]  --->  String  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR
print(a [2 : 8])  #  a[2 : 8  : 1]  -->  String  from  indexes  2  to  7  in  steps  of  1  i.e. ma<space>Rao
print(a [2 : 8 : -1]) #  String  from  indexes  2  to  9  in  steps  of  -1   i.e.  Empty  string
print(a [ : -6 : -1])  #  a[-1 : -6 : -1]  --->  String  from  indexes   -1   to  -5   in  steps  of  -1   i.e.  oaR<space>a
print(a [2 : -3])  #  a[2 : -3 : 1]  --->  String  from  indexes  2  to   -4   in  steps  of  1  i.e. ma<space>
print(a [1 : 6 : 2])  #   String  from  indexes  1  to  5  in  steps  of  2  i.e. aaR
print(a [ : -5 : -5])  #  a[-1 : -5 : -5]  --->  String  from  indexes  -1  to  -4   in  steps  of  -5    i.e. o
print(a [2 : -5])  #  a[2 : -5 : 1]  --->  String  from  indexes  2  to  -6  in  steps  of  1  i.e. m
print(a [2 : -5 : 2])  #  String  from  indexes  2  to  -6  in  steps  of  2  i.e. m
print(a [ : 0 : -1])  #  a[-1 : 0 : -1]  --->  String  from  indexes  -1   to   1  in  steps  of  -1   i.e.  oaR<space>ama
print(a [-5 : 0 : -2])  #   String  from  indexes  -5  to  1   in  steps  of  -2  i.e.aa
