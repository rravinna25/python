#  What  are  the  outputs  if  inputs  are  25 , Rama  Rao ,  male , 52 , 48 , 55   (Home  work)
from  prog9a  import  student  #  Imports  student  class  and  the  if  statement  outside  the  student  class  in  prog9a
s = student()  #  Creates  an  empty  student  class  object
print(s . __dict__) #  {}  :  's'  is  an  empty  object
s . get()  #   Adds  variables  rno , sname ,  gender  and  list  'm'  to  object  's'  with  user   inputs
print(s . __dict__) #  {'rno': 25, 'sname': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55]}
s . compute() # Adds  variables  tot , avg ,  grade  to  object  's'  with  results
print(s . __dict__)  #  {rno': 25, 'sname': 'Rama Rao', 'gender': 'm', 'm': [52, 48, 55], 'tot': 155, 'avg': 51.66, 'grade': 'Second  class'}


# Object  's'   --->  rno = 25, sname  = 'Rama  Rao' , gender = 'm'  , m = [52 , 48 , 55] , tot = 155 , avg = 51.66 , grade  = '2nd  class'


'''
1) How  many  variables  are  added  to  object  's'  by  get()  method ?  --->  4  i.e. rno , sname , gender   and  m (list)

2) How  many  variables  are  added  to  object  's'  by  compute()  method ?  --->  3  i.e. tot , avg  and  grade
'''
