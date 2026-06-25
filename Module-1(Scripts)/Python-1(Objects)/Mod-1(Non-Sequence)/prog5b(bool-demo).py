# bool object demo program
a = True   #  Ref 'a'  points  to  object  True
print(a)  #  Value  of  object  'a'   i.e. True
print(type(a)) # Type of object 'a' i.e.  <class  'bool'>
print(id(a)) # Address of object   True
a = False  #  Ref  'a'  is  modified  to  object   False
print(b)   #   Value  of  object  'a'  i.e. False
print(type(a))  # Type of object 'a' i.e.  <class  'bool'>
print(True + True)  # 1 + 1  = 2
print(True + False) # 1 + 0  = 1
print(False + True)  # 0 + 1 = 1
print(False + False) # 0 + 0 = 0
print(True + True + True) # 1 + 1 + 1  = 3
print(25 + 10.8 + True) #  36.8
print(True > False) # 1 > 0  is  True
print(True)  #  True
print(False) #  False
#print(true)  #  Error  due  to   't'
#print(false) #  Error  due  to   'f'



'''
1) When  are  True  and  False  treated   as  1  and  0  ?  ---> When  operations  are  made  on  True  and  False

2) When  are  True  and  False  not  treated   as  1  and  0  ?  ---> When  operations  are  not  made  on  True  and  False
'''
