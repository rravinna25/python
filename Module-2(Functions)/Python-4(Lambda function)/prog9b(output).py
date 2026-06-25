# Find outputs  (Home  work)
x = 5
adder1 = lambda  y , x = x  : x + y   #  default  value  of  'x'  is  5
x = 10
adder2 = lambda  y , x = x : x + y    #  default  value  of  'x'  is  10
x = 20
print(adder1(100)) #   Executes  lambda  function  with  y = 100 , x = default  value  5  which  returns  5 + 100 = 105
print(adder2(200))  #   Executes  lambda  function  with  y = 200 , x = default  value  10  which  returns  10 + 200 =  210
print(adder1(300 , 400)) # Executes  lambda  function  with  y = 300 , x = 400  which  returns  400 + 300 =  700
