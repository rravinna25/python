# Find  outputs  (Home  work)
a = {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(a) #  {10 : 'Ramesh' , 20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}
print(type(a)) # <class 'dict'>
print(a[10]) #  Value  of   key  10  i.e. Ramesh
print(a[20]) #   Value of   key  20  i.e Kiran
print(a[15]) #   Value  of   key  15  i.e Amar
print(a[18]) #   Value  of  key  18  i.e sita
#print(a[19]) # Error :  Key  19  does  not  exist  in  dict  'a'
#print(a[0]) # Error :  Key  0  does  not  exist  in  dict  'a'
#print(a['Amar']) # Error :  Key  'Amar'  does  not  exist  in  dict  'a'
a[15] = 'Krishna' #   Value of   key  15  is  modified  to  'Krishna'  in  dict  'a'
del   a[20] #   Removes  20 :  'Kiran'   from  dict  'a'
a[25] = 'Vamsi' #   Appends  25 : 'Vamsi'  to  dict  'a'
print(a)   #  {10 : 'Ramesh', 15 : 'Krishna', 18 : 'Sita' , 25:'Vamsi'}
print(len(a)) #  4
#print(a * 2) # Error :  Dict  can  not  be  repeated  as  duplicate  keys  are  obtained  when  it  is  repeated
