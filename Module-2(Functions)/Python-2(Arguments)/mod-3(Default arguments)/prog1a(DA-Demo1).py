# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100)) #   'a'  is  100  , 'b'  is  default  value  20 , 'c'  is  default  value  30 , Result  is  150
print(add(100 , 200)) # 'a'  is  100 , 'b'  is  200 , 'c'  is  default  value  30 , Result  is  330
print(add(100 , 200 , 300)) # 'a'  is  100 , 'b' is  200 , 'c'  is  300 , result  is  600
print(add(100 , c = 200)) # 'a'  is  100 , 'b'  is  default  value  20 , 'c'  is  200 , result  is  320
print(add(c = 100 , b = 200 , a = 300)) # 'a'  is  300 , 'b' is  200 , 'c'  is  300 , result  is  600
print(add(c = 100 , a = 200)) # 'a'  is  200 , 'b' is  deafult  value  20 ,  'c'  is  100 , result  is  320
#print(add()) # Error :  Arg  is  not  passed  for  'a'
#print(add(a = 100 , 200)) # Error:  Positonal argument  200 is  not  permitted  after keyword argument  a = 100
#print(add(100 ,  , 300))    #  Error  due  to  two  commas
#print(add(100 ,  b , 300)) # Error : Object  'b'  does  not  exist
