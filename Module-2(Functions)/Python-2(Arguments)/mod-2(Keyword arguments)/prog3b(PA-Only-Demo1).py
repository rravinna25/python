#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a  :  10  <tab>  b  :  20
#f1(a = 30 ,  b = 40) # Error :  Function  f1()  expects  positional  arguments  but   a = 30 , b = 40  are  keyword  args
#f1(50 , b = 60) # Error :  Function  f1()  expects  positional  arguments  but   b = 60   is  keyword  arg
#f1(a = 70 , 80) # Error :  Positional argument  80  is  not  permitted   after  keyword argument a = 70
