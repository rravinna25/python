 #Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a  :  10  <tab>  b :  20  <tab>  c  :  30
f1(a = 40 , b = 50 , c = 60) # a  :  40  <tab>  b :  50  <tab>  c  :  60
f1(c = 100 , b = 90 , a = 80) # a  :  80  <tab>  b :  90  <tab>  c  :  100
#f1(70 , 80 , c = 90)  # Error :  Function  f1()  expects  keyword  arguments  for  'b'  and  'c'   but  80  is  positional argument  
#f1(70 , 80 , 90) # Error :  Function  f1()  expects  keyword  arguments  for  'b'  and  'c'   but  80  and  90  are  positional arguments
#f1(c = 15 , b = 25 , 35) # Error :  PA  35  is  not  permitted  after  KA  b = 25
