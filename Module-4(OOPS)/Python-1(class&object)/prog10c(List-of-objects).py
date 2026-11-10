'''
Repeat  prog10a  with  list  of  6  objects

Hint: Reuse  Rat  class  defined  in  prog10a  but  do  not  rewrite  the  class  again

What  are  the  object  names  ?  --->  a[0] , a[1] , a[2] , .....a[5]
'''
from  prog10a  import  rat  #  imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = [rat()  , rat() , rat() , rat() , rat() , rat()]  #  Creates  a  list  of  6  rat  class  objects
a[0] . get()   #  Reads  numerator  and  denominator  into   object  a[0]
a[1] . get()   #  Reads  numerator  and  denominator  into   object  a[1]
a[2] . add(a[0] , a[1]) #  Adds  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[2]
a[3] . sub(a[0] , a[1]) #  Subtracts  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[3]
a[4] . mul(a[0] , a[1]) #  Multiplies  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[4]
print('Sum : ' , a[2])  #   __str__()  method  returns  values  of  object   a[2]  in  the  form  of   string
print('Difference :  ' , a[3])  #   __str__()  method  returns  values  of  object   a[3]  in  the  form  of   string
print('Product :  '  ,  a[4])  #   __str__()  method  returns  values  of  object   a[4]  in  the  form  of   string
if  a[1] . nr == 0:
	print('Division  is  not  permitted')
else:
	a[5] . div(a[0] , a[1])  #  Divides  rational   numbers  in  objects   a[0]  and   a[1]  and  stores  results  in  object  a[5]
	print('Division :  ' , a[5])  #   __str__()  method  returns  values  of  object   a[5]  in  the  form  of   string


'''
Object  a[0]   --->  nr = 2 , dr = 3

Object  a[1]   --->  nr = 5 , dr = 9

Object  a[2]   --->  nr = 11 , dr = 9

Object  a[3]   --->  nr = 1 , dr = 9

Object  a[4]   --->  nr = 10 , dr = 27

Object  a[5]   --->  nr = 6 , dr = 5


def  add(self , a , b):
		pass
a[2] . add(a[0] , a[1])
What  are  self ,  a   and  b  for  the  above  method  call  ?  --->  self  is  a[2]  ,  a  is  a[0]  and    b  is  a[1]
'''
