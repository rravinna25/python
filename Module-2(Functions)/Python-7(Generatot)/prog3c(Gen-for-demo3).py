# Find  outputs (Home  work)
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End of  generator
for  x  in  f1(): #  'x'  is  each  element  of  1st  generator  object  created  by   f1()
	print(x)  #   25  <next  line>  10.8 <next  line>  Hyd <next  line>
for  x  in  f1():  #  'x'  is  each  element  of  2nd  generator  object  created  by   f1()
	print(x)  #   25  <next  line>  10.8 <next  line>  Hyd <next  line>
for  x  in  f1():  #  'x'  is  each  element  of  3rd  generator  object  created  by   f1()
	print(x)  #   25  <next  line>  10.8 <next  line>  Hyd <next  line>


'''
1) How  many  generator  objects  are  in  the  program ?  --->  Three

2) What  does  f1()  do ?  --->  Creates  an  empty  generator  object
'''
