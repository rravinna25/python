# complex object demo program
a = 3 + 4j   #  Ref  'a'  points  to  object  3 + 4j
print(a)	 #  3+4j
print(type(a))   # Type of object 'a' i.e.  <class 'complex'>
print(id(a))  # Address of object  3 + 4j (may be 1000)
print(a . real) # 3.0
print(a . imag) # 4.0
print(type(a . real)) # <class  'float'>
print(type(a . imag))  # <class  'float'>
#print(type(a . imaginary))   #  Error :  No  field  imaginary


'''
What  is  the  type  of  real  and  imag  ?  --->  Always  float
'''
