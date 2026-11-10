# setattr() , getattr()  and  hasattr()  functions  demo  program
class  emp:
        pass
# End of  the class
e = emp()  #  Creates  an  empty  emp  class  object
print(e . __dict__)  #  { }
setattr(e , 'empno' , 25)  #  Adds   variable  empno  to  object  'e'   with  value  25  (Same  as  e . empno = 25)
setattr(e , 'ename' , 'Rama  Rao')  #  Adds  variable  ename   to  object  'e'   with  value   'Rama  Rao'  (Same  as  e . ename =  'Rama Rao')
setattr(e , 'sal' , 10000.0)  #  Adds   variable  sal   to  object  'e'   with  value   10000.0  (same  as  e . sal = 10000.0)
setattr(e , 'sal' , 20000.0)  # Modifies  variable  sal  of  object   'e'  to 20000.0  (same  as  e . sal = 20000.0)
print(e . __dict__)  #  {'empno' : 25 , 'ename' : 'Rama Rao' , 'sal' : 20000.0}
print('emp  number  :  ' , getattr(e , 'empno'))   #  Returns  value of  empno in  object  'e'   i.e.  25
print('emp  name    :  ' , getattr(e , 'ename'))   #  Returns  value of  ename  in  object  'e'   i.e.   Rama  Rao
print('Salary  :  ' , getattr(e , 'sal'))   #  Returns  value of   sal   in  object  'e'   i.e.   20000.0
#print('Gender  :  ' , getattr(e , 'gender'))  #   Error :  Object  'e'  does  not  have  gender  variable
print(hasattr(e , 'empno')) #   True :   Object  'e'  has  variable  empno 
print(hasattr(e , 'ename'))   #  True  :   Object  'e'  has  variable  ename
print(hasattr(e , 'sal'))  #  True :  Object  'e'  has  variable  sal 
print(hasattr(e , 'gender'))  #  False : Object  'e'  does  not  have  variable  gender
