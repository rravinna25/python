# Find  outputs
a = 0B10101  #   Object  contains  decimal  equivalent  i.e.  16 + 4 + 1 = 21
print(a)  #  21
print(type(a))  #   <class  'int'>
print(id(a))   #  Address  of   object  21  (may  be  1000)
b = 0b10101   #   Ref  'b'  points to same  object  becoz  number  is  same
print(b)  #  21
print(id(b))  #  Same  address   (1000)
c = 21     #   Ref  'c'  points to same  object  becoz  number  is  same
print(c)  #   21
print(id(c))  #  Same  address   (1000)
d = 10101  #  Decimal  number
print(d)  #   10101
#e = 0B1234   #  Error  due  to 2  , 3  and  4


'''
1) Conversion  of  binary  number  to  decimal
    ---------------------------------------------------
        16    8     4    2     1   --->  Weights
		1     0      1    0     1   --->	16 + 4 + 1 = 21

2) a = 0B10101
    b = 0b10101
    c = 21
    How  many  objects  are  there  ? --->  Single  object  with  three  references  and
                                                                  all  the  three  references  point  to  the  same  object
'''
