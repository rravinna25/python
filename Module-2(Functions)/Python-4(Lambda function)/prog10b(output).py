#  Find  outputs
def   f1():
	print('Hyd')
def   f2():
	print('Sec')
# End  of  the  function	
a = ['f1' , 'f2']  #  List  of  two  strings
print(a)  # ['f1' , 'f2']
b = [f1 , f2]  #  List  of  2  functions
for  x  in  b:   # 'x'  is  each  function  of   list  'b'
	     x()  #  Executes  each  function  
#c = [def   f3():  print('Hyd') ,  def   f4():  print('Sec')]  #  Error :  Functions  can  not  be  defined  in  the  list
d = [f1() , f2()] #  Executes  both  the  functions  and  it  is  list  of  2  None's
print(d)  #  [None , None]
e = [lambda  x :  x ** 2 , lambda  x :  x ** 3]  # List  of  lambda  functions
print(e) #  [Type  and  address  of  first  lambda  function,  Type  and  address  of  2nd  lambda  function]
for  x  in   e:   # 'x'  is  each   lambda  function  of   list  'e'
	print(x(5))  #  Executes  each  lambda  function  

'''
['f1', 'f2']
Hyd
Sec
Hyd
Sec
[None, None]
[Type  and  address  of  first  lambda  function , type  and  address  of  2nd  lambda  function]
25
125


1) Which  functions  can  be   defined  in  the  list ?  ---> Lambda  functions  but  not  regular  functions

2) a = ['f1' , 'f2']
    b = [f1 , f2]
    c = [f1() , f2()]
    d = [def  f1():  print('Hyd') , def  f2(): print('Sec')]
    e = [lambda  x :  x ** 2 , lambda  x :  x ** 3]
	What  is  the  difference ?  --->  'a'  is  list  of  function  names,
	                                                    'b'  is  list  of  regular  functions ,
														'c'  is  list  of   results  of  the  two  functions,
														'd'  is  list  of  function  definitions  which  is  not  permitted  and
														'e'  is  list  of  lambda  functions
'''
