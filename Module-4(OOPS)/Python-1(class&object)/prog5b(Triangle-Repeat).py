'''
Repeat  prog5a  such  that  methods  are  called  in  another  way

1) What  are  the  two  ways  to  call  a  method ?  --->  object . method()  and  classname . method(object)

2) Import  triangle  class  defined  in  prog5a  but  do  not   define  triangle  class  again
'''
from  prog5a   import  triangle  #  Imports  triangle  class  and  the  if  statement  present  outside  triangle  class
t = triangle() #  Creates  empty  triangle  class  object
triangle . get(t) #  Executes  get()  method  of  triangle  class  and  passes  object  't'  to  the  method
triangle . test(t) #  Executes  test()  method  of  triangle  class   and  passes  object  't'  to  the  method
print('Area : ',  triangle . area(t) )  #  #  Executes  area()  method  of  triangle  class  and  passes  object  't'  to  the  method
print('Perimeter: ', triangle . peri(t)) #  Executes  peri()  method  of  triangle  class   and  passes  object  't'  to  the  method


#  Object  't'  --->  a = 3.0 , b  =  4.0  ,  c  = 5.0


'''
1) from  prog5a  import  triangle
	What  are  imported ?  --->  triangle  class   and  the  if  statement  which  is  outside  triangle  class

2) py  prog5a.py
    What  is  the  value  of  __name__  variable ?  --->  '__main__'  becoz   module  prog5a  is   being  executed

3) from  prog5a  import  triangle
    What  is  the  value  of  __name__  variable ?  ---> 'prog5a'
     Is  if   statement  executed ?  ---> No  becoz  if  condition  is   false

*4) In  general, statements  outside   the  class  should  be  under  if  condition  so  that
      they  are  not   executed  when  the  program  (or)  module  is  imported  elsewhere

5) classes , functions  and  objects  defined  in  a  program  can  be  reused  by  a   different  program.
    This  is  possible  with  import  (or)  from  statement

6) import  prog5a
    What  are  imported ?  --->  prog5a  and  if  statement
    Is  triangle  class  imported ?  ---> No  becoz  members  are  not  imported
    How  to  use  triangle  class ?  --->  prog5a . triangle
'''
