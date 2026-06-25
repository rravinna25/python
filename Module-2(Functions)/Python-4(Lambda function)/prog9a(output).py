# Tricky  porgram
# Find  outputs
x = 5
adder1 = lambda    y  :  x + y
x = 10
adder2 = lambda    y  :  x + y
x = 20
adder3 = lambda    y  :  x + y
print(adder1(100)) #  120  : Executes  lambda  function  with  y = 100  and  result  is  20 + 100 
x = 30
print(adder2(200))  # 230 : Executes  lambda  function  with  y = 200  and  result  is  30 + 200 
x = 40
print(adder3(300))  # 340 : Executes  lambda  function  with  y = 300  and  result  is  40 + 300 



'''
1) What  is  the  value  of  'x'  when  adder1  is  called ?  --->  20  but  not  5
    Why  not  5  ?  --->  'x'  is  5  when  adder1  is  defined  but  not  when  it  is  called

2) What  is  the  value  of  'x'  when  adder2  is  called ?  --->  30  but  not  10
     Why  not  10  ?  --->  'x'  is  10  when  adder2  is  defined  but  not  when  it  is  called

3) What  is  the  value  of  'x'  when  adder3  is  called ?  --->  40  but  not  20
     Why  not  20  ?  --->  'x'  is  20  when  adder3  is  defined  but  not  when  it  is  called

4) In  general ,  value  of  'x'  at  the  time  of  function  call  matters  but  not  value  of  'x'  at  the  time  of  function 
    definition
'''
