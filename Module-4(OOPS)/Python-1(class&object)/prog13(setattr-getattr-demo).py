#  Find  outputs  (Home  work)
class    c1:
        pass
# End  of  the  class
a = c1()  #  Creates  an  empty  c1  class  object
a . x = 10 #  Adds  variable  'x'  to  object  'a'  with  value  10
varname = input('Enter  variable  name  to  be  added  to  object  :  ')   #  Assume  that  input  is  'y'
value = eval(input('Enter  value  of  the  variable  :  '))   #  Assume  that  input  is   20
setattr(a , varname , value)  #  Adds  variable  'y'  to  object  'a'  with  value   20
print(a . __dict__)  #  {'x' : 10 , 'y' : 20}
print(a . x) # 10
while  True:
	try:
		varname = input('Enter  variable  name  whose  value  is  to  be  retrieved  :  ')   #  Assume  that  input  is  x  in  1st   iteration  ,  y  in   2nd   iteration  and  z  in  3rd  iteration
		print(getattr(a , varname))
	except:
		print(F'Invalid  variable   name   :  {varname}')
		break

# Object   'a'   --->  x = 10 , y = 20

'''
{'x': 10, 'y': 20}
10
10  if  user  input  is  'x'
20  if  user  input  is  'y'
Invalid  variable   name   :  z  if  user  input  is  'z'
'''
