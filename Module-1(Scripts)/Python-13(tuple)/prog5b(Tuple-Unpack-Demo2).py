# Find outputs
tpl = 25 , 10.8 , 'Hyd' , True
a , b , *c = tpl  #  Unpacks  tuple  to  3  elements
print(a)  #   25
print(b) #  [10.8 , 'Hyd']
print(c)  #  True
print(type(c)) #  <class  'list'>


'''
What  is  obtained  when  tuple  is  unpacked  with  *  operator ?  --->  List
'''
