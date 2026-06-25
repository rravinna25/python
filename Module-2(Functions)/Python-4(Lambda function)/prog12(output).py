# Find  outputs  (Home  work)
def   f1(x):
        return  lambda  n  :  x ** n
lamb = f1(3) #   Executes  function  f1()  with  x = 3  which  returns  lambda  function  i.e. lamb =  lambda  n  :  3 ** n  --->  Ref  lamb  points  to  lambda  function
print(type(f1)) # <class 'function'>
print(type(lamb)) # <class 'function'>
print(lamb(2)) #  Executes  lambda  function  with  n = 2  which  returns  3 ** 2 = 9 
print(lamb(5)) #  Executes  lambda  function  with  n = 5  which  returns  3 ** 5 = 243
print(lamb) # Type  and  address  of  lambda  function
#print(lamb()) #  Error :  Argument  is  not  passed for  'n'


'''
1) Function  f1() returns  lambda  function  which  is  assigned  to  lamb

2) lamb(2)  executes  lambda   function
'''
