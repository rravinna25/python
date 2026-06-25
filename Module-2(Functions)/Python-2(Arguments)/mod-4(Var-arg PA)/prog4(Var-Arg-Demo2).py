#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40) # a : 10 <tab> b : (20 , 30 , 40)
f1(50 , 60) # a : 50 <tab> b : (60,)
f1(70) # a:70 <tab> b : ()
f1(a = 80) # a : 80 <tab> b : ()
#f1(b = (10 , 20 , 30) , a = 40) #  Error :  var-arg  parameter  'b'  can  not  be  a   keyword argument
f1() # a :  default  value  25 <tab> b : ()
#f1(a = 10 , (20 , 30 , 40))  # Error :   PA  (20 , 30 , 40)  is  not  permitted  after  KA  a = 10
#f1(35 , b = (10 , 20 , 30)) #  Error :  var-arg  parameter  'b'  can  not  be  a   keyword argument
#f1(25 , a = (10 , 20 , 30))  #  Error :  'a'  is  already  25   and  hence  'a'  can  not  be  (10 , 20 ,  30)
f1((10 , 20 , 30) , 10 , 20 , 30)  #  a : (10 , 20 , 30) <tab> b : (10 , 20 , 30)
#f1(a = (10 , 20 , 30) , 40 , 50 , 60) # Error :  PA  40  is  not  permitted  after  KA   a = (10 , 20 , 30)


'''
def   f1(a = 25  , *b):
        pass
1) f1(PA , KA)
    Is  the  function  call  valid ?  --->  No  becoz  'b'  can  not  be  KA  as  it  is  var-arg  parameter

2) f1(PA , PA)
    Is  the  function  call  valid ?  ---> Yes

3) f1(KA , PA)
    Is  the  function  call  valid ?  --->  No  becoz  PA  is  not  permitted  after  KA

4) What  is  the  conclusion ?  --->  Argument  before  var-arg  parameter  should  be  PA  only
'''
