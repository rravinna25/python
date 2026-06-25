# Find  outputs  (Home  work)
a = 0XA7B9   #  Object  contains  decimal  equivalent  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(a)  # 42937
print(type(a)) # <class 'int'>
b = 0xBEEF   #  Object  contains  decimal  equivalent  i.e.  11 * 16 ^ 3 +  14 * 16 ^ 2 + 14 * 16 ^ 1 +  15 * 16 ^ 0 = 48879
print(b)  # 48879
#print(A7B9) #  Error :   Object  A7B9  does  not  exist
print('A7B9') # A7B9
#print(0XBEER) #  Error due to  'R' in hexa-decimal number
#print(0XHYD) #   Error due to 'H'  and  'Y' in hexa-decimal number
#print(0xA7G9B)  #  Error due to 'G'  in  hexa-decimal number


'''
Conversion   of   hexa  decimal  number  to  decimal
-------------------------------------------------------------
     4096   256    16     1  --->  Weights
      A         7       B      9  --->  10 * 4096 + 7 * 256 + 11 * 16 + 9 * 1 = 42937
'''
