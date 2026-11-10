#  Find  outputs (Home  work)
class   c1:
	def  __str__(self):  #  self  is  object  'a'
			return  '25'
class   c2:
	def  __str__(self):  #  self  is  object  'b'
			return   35
class   c3:
	def  __str__(self):  #  self  is  object  'c'
			print('Hyd')
class   c4:
	def  __str__(self , x):    #  self  is  object  'd'  and  'x'  is   50
			return   F'{x}'
#end of the class
a = c1()  # Creates  an  empty  c1  class  object
b = c2()  # Creates  an  empty  c2  class  object
c = c3()   # Creates  an  empty  c3  class  object
d = c4()    # Creates  an  empty  c4  class  object
print(a) #  __str__()  method  of  c1  class  returns   '25'
#print(b) #  Error :   __str__()  method  of  class  c2   returns  non-string  i.e.  35
#print(c)  #  Error  :   __str__()  method  of  class  c3   returns  non-string  i.e.  None
#print(d) # Error  :   __str__()  method  of  class  c4  has  an  arg  'x'
print(b . __str__()) #  __str__()  method  of  class  c2  returns  35
print(c . __str__())  #  __str__()  method  of  class  c3  prints  'Hyd'  and  returns  None
print(d . __str__(50))  #   __str__()  method  of  class  c4  returns   '50'


'''
25
35
Hyd
None
50


1) Can  __str__()  method  return  non-string ?  --->  Yes  when  it  is  called  explicitly  and
                                                                                    no  when  it  is  automatically  executed

2) Can  __str__()  method  have  an  argument ?  ---> Yes  when  it  is  called  explicitly  and
                                                                                    no  when  it  is  automatically  executed
'''
