# Find outputs (Home  work)
def  f1():
        global  a  #  Treats  'a'  as  Gv
        print(a) #  Gv  i.e. 11
        a += 1  #  Modifies  Gv  to  12
def  f2():
        global  a #  Treats  'a'  as  Gv
        print(a) #  Gv  i.e. 13
        a += 1  #  Modifies  Gv  to  14
# End  of  the  function
a = 10 #  Creates  Gv  with  value  10
print(a) #  Gv  i.e.  10
a += 1 #  Modifies  Gv  to  11
f1()
print(a) #  Gv  i.e. 12
a += 1  #  Modifies  Gv  to  13
f2()
print(a) #  Gv  i.e. 14


'''
10
11
12
13
14
'''
