# Which  of  the  following  are  valid  ?  (Home  work)
'''
def   f1(*a , *b): #  Error :  Multiple  *'s   are  not  permitted  in  the  function  header
        pass
'''
def  f2(*a , b): #  Valid  due  to  single  *
        pass
def  f3(a , *b): #  Valid  due  to  single  *
        pass
def  f4(a , b):  #  Valid
        pass
def    f5(a , *b , c):  #  Valid  due  to  single  *
        pass
'''
def   f6(* , a , *b , c): # Error :  First  *  demands  a , b.  and  c  to  be  ka's   but  'a'  and  'b'  can  not  be  KA's
       pass
def   f7(a , *b , c ,  /): # Error :  /  demands  a , b.  and  c  to  be  pa's   but 'c'  can  not  be  a  pa
       pass



1) How  many  var-arg  parameters  can  be  in  a  function ?  ---> At  most  one

2) def   f6(* , a , *b , c):
		pass
   What  does  first  *  indicate ?  --->  a , b , c  should  be  KA's  only
   Can  'b'  be  a  keyword  argument ?  --->  No  becoz  var-arg   parameter  should  be  PA  only
   Can  'a'  be  a  keyword  argument ?  --->  No  becoz  it  is  before  var-arg  parameter

3) def   f7(a , *b , c ,  /):
           pass
    What  does  /  indicate ?  --->  a , b  and  c  should  be  PA's  only
    Can  'c'  be  a  positional  argument ?  --->  No  becoz  argument  after  var-arg  parameter  should  be  a  KA  only
'''
