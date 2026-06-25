# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10  <tab>  b :  20  <tab> c  :  30
f1(40 , 50 , c = 60) # a  :  40  <tab>  b :  50  <tab> c  :  60
#f1(a = 70 , b = 80 , c = 90) # Error : Function  f1()  expects  positional  arguments  for  'a'   and  'b'  but  a = 70  and  b = 80  are  keyword  arguments
#f1(a = 100 , b = 110 , 120) # Error :   PA  120  is  not  permitted  after  KA  b = 110
#f1(a = 130 , 140 , c = 150) # Error :  PA  140  is  not  permitted  after  KA  a = 130
#f1(160 , b = 170 , 180) # Error : PA  180  is  not  permitted  after  KA  b = 170
#f1(190 , b = 200 , c = 210)  # Error : Function  f1()  expects  positional  arguments  for  'b'   but  b = 200  is  keyword  argument
