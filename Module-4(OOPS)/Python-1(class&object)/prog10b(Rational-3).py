'''
Repeat  prog10a  with  3  objects

Eg:  c = a + b
	 print  c
	 c = a - b
	 print  c
	 c = a * b
	 print  c
	 c = a / b
	 print  c

Hint:  Import   rat  class  defined  in  prog10a  but  do  not  define  rat  class   again
'''
from  prog10a  import  rat  #   imports  rat  class  and  if  statement  outside  rat  class  in  prog10a
a = rat()  #  Creates  3  empty  rat  class  objects
b = rat()
c = rat()
a . get()  #  Reads  numerator  and  denominator  into   object  'a'
b . get()  #  Reads  numerator  and  denominator  into   object  'b'
c . add(a , b)  #  Adds  rational  numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Addition : {c}') #   __str__()  method  returns  values  of  object  'c'  in  the  form  of   string
c . sub(a , b)  #  Subtracts  rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Substraction : {c}')  #   __str__()  method  returns  values  of  object  'c'  in  the  form  of   string
c . mul(a , b)  #  Multiplies   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
print(F'Multiplication : {c}')   #   __str__()  method  returns  values  of  object  'c'  in  the  form  of   string
if  b . nr == 0:
	print('Division  is  not  permitted')
else:
	c . div(a , b)  #  Divides   rational   numbers  in  objects  'a'  and  'b'  and  stores  results  in  object  'c'
	print(F'Division : {c}')  #   __str__()  method  returns  values  of  object  'c'  in  the  form  of   string


'''
Object   'a'  --->  nr = 2 , dr = 3

Object   'b'  --->  nr = 0 , dr = 9


from  prog10a   import  rat
Is  if  statement  of  prog10a  executed ?  --->  No  becoz  if  condition  is  false
'''
