# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 'a'  is  2  ,  'b'  is  6  and  result  is  2 ** 6 = 64
print(power(5))  # 'a'  is  5  , 'b'  is   default  value  2  and  result  is  5 ** 2 = 25
print(power(b = 3 , a = 4.5))  # 'a'  is  4.5     'b'  is  3  and  result  is  4.5 **3 = 91.125
print(power(3 + 4j)) # 'a'  is   3 + 4j ,   'b'  is  default  value  2 and  result  is  (3+4j)**2 = 9 + 12j + 12j - 16 = -7 + 24j
print(power(True))  # 'a'  is   True  ,  'b'  is   default  value  2  and  result  is  True ** 2 = 1
'''
def   power(b = 2 , a): # Error :  Non-default  arg  'a'   is  not  permitted  after  default  arg  b = 2
 	 pass
'''
