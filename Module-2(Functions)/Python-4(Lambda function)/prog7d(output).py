# Find  outputs   (Home  work)
a  =  lambda  :  print('Hyd')  , print('Sec')  , print('Cyb')  #   'a'  is  tuple  of  3 elements  i.e. (lambda  function , None , None)
print(type(a))  # <class 'tuple'>
print(a)  #(Type and address of  lambda function , None ,None)
for  x  in  a:  #  'x'  is  each  element  of  tuple  'a'
	print(x) # type and address of  lambda function <next line> None <nextline> None
#a() # Error :  Tuple  can  not  called  as  it  is  not  a   function
print(a[0]())  #  Executes  lambda  function  which  prints  'Hyd'  and  retutns  None  i.e.  print(None)  prints  None


'''
Sec
Cyb
<class  'tuple'>
(type and address of  lambda function , None ,None)
type and address of  lambda function
None
None
Hyd
None
'''
