# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a  :  10   <tab>  b :  20
f1(b = 30 , a = 40) # a  :  40  <tab>  b :  30
#f1(50 , 60) # Error :  Function  f1()  expects  keyword  arguments  but  50  and  60  are  positional  args
#f1(70 , b = 80) # Error :   Function  f1()  expects  keyword  arguments  but   70  is  positional  argument
#f1(a = 15 , 25) # Error :  Positional  argument  25  is  not  permitted  after  keyword  argument  a = 15
