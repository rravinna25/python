# Find  outputs  (Home  work)
a = 'Hyd'  #  Ref 'a'  points  to  object  'Hyd'
print(id(a))  #  Address of object  'Hyd'
#a[1] = 'e' # Error :  Char  of  string   can  not  be  modified  as  str  is  immutable
a = 'Sec'  #   Modifies  ref  'a'  to  object  'Sec'
print(id(a))  #  Address of object  'Sec'
b = (10 , 20 , 15 , 18)  #  Ref 'b'  points  to   tuple
print(id(b)) #  Address of   tuple  (10 , 20 , 15 , 18)
#b[2] = 19 # Error :  Element  of  tuple  can  not  be  modified  as   tuple  is  immutable
b = (30 , 40 , 35 , 32)  #   Modifies  ref   'b'  to  another  tuple
print(id(b))  #  Address of   2nd  tuple  (30 , 40 , 35 , 32)
c = range(5)  #  Ref 'c'  points  to   1st   range  object
print(id(c))  #  Address  of  1st  range  object
#c[3] = 10 # Error  :  Element  of   range  object  can  not be  modified  as  range object is immutable
c = range(5)  #   Modifies  ref  'c'  to  2nd  range  object
print(id(c))    #  Address  of  2nd  range  object


'''
1) a = 'Hyd'
    a = 'Sec'
    What  is  modified  when   a = 'Sec'  is  executed  ?  ---> Reference  but  not  object

2) b = (10 , 20 , 15 , 18)
    b = (30 , 40 , 35 , 32)
    What  is  modified  when  b = (30 , 40 , 35 , 32)  is  executed  ?  --->  Reference  but  not  object

3) c = range(5)
    c = range(5)
    What  is  modified  when  c = range(5)  is  executed  ?  --->  Reference  but  not  object
'''
