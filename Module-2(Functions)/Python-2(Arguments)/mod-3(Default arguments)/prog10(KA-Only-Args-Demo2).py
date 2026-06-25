# Find  outputs(Home  work)
'''
def   add(a = 10 , b , c): # Error : Non-default  arguments  b  and  c  are  not  permitted  after  default  argument  a = 10
        pass
'''
def   add( * , a = 10 , b , c ): #   Order  is  not  important  due  to  *
        return  a + b + c
#End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) #  'a'  is  30 , 'b'  is  40 , 'c' is  50 , result  is  120
print(add(b = 60 , c = 70)) #  'a'  is  default  value  10 , 'b'  is  60 , 'c' is  70 , result  is  140
print(add(c = 80 , b = 90 , a = 100))  #  'a'  is  100 , 'b'  is  90 , 'c' is  80 , result  is  270
#print(add(c = 25 , a = 43)) # Error :  Argument  is  not  passed  for  'b'
#print(add(1 , 2 , 3)) # Error  :   Positional  rguments  can  not  be  passed  due  to  *  in  the  function header
'''
def   add(a , b = 10 ,  c , * , d  , e = 20 , f): # Error :  Non-default  argument  'c'   is  not  permitted   after  default  argument   b = 10
		pass
'''

'''
What  are  the  two   advantages  of  *  in  the  function  header ?  ---> 
												1) Non-default  arguments  and  default  arguments  can  be  in  any  order
												2) PA's  can  not  be  passed  to  the  function
'''
