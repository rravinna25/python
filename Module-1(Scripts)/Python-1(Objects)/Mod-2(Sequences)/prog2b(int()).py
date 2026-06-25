# int()  function  demo  program
print(int(10.8))   #  Converts  10.8  to  10
print(int(True))    #  Converts   True  to   1
print(int(False)) # Converts False to 0
print(int('25')) #  Converts  '25'  to  25
print(int('0075')) #  Converts  '0075'  to   75
print(int(0B11010)) #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(0B11010)  #  Converts  binary  number  to  decimal  number  i.e.  16 + 8  + 2 = 26
print(int(0O6247))  #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(0O6247)   #  Converts  octal  number  to  decimal  number  i.e.  6 * 8 ^ 3 + 2  * 8 ^ 2 + 4 * 8 ^ 1 + 7 * 8 ^ 0  = 3239
print(int(0XA7B9))   #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
print(0XA7B9)  #  Converts  hexa-decimal  number  to  decimal  number  i.e.  10 * 16 ^ 3 + 7 * 16 ^ 2 + 11 * 16 ^ 1 + 9 * 16 ^ 0 = 42937
#print(int(3 + 4j)) #  Error  :  complex  number  can not be converted to int
#print(int('25.4')) #  Error :  string  float  can not be converted to int
#print(int('Ten'))  #  Error :  'Ten'  can not be converted to int


'''
int()  function
----------------
1) What  does  int(x)  do  ?  --->  Converts  object  'x'  to  integer

2) Conversion  of  binary  number  to  decimal  number
    ----------------------------------------------------------
          16    8   4   2    1  --->  Weights
	       1     1    0   1    0   --->  16 + 8 + 2 =  26

3) Conversion  of  octal  number  to  decimal  number
    ---------------------------------------------------------
        512   64   8    1  --->  Weights
	      6      2    4   7  --->  6 * 512 + 2 * 64 + 4 * 8 + 7 * 1  = 3239

4) Conversion  of  hexa-decimal  number  to  decimal  number
    ------------------------------------------------------------------
        4096   256   16    1  --->  Weights
	      A        7      B     9  --->  10 * 4096 + 7 * 256 + 11 * 16 + 9 * 1  = 42937
		  
5) Is  int()  function  needed  to  convert  binary  number  to  decimal  number  ?  --->  
																					No  becoz  print(binary-number)  any  prints  decimal  equivalent		  

6) Is  int()  function  needed  to  convert  octal  number  to  decimal  number  ?  --->  
																					No  becoz  print(octal-number)  any  prints  decimal  equivalent		  
																					
7) Is  int()  function  needed  to  convert  hexa-decimal  number  to  decimal  number  ?  --->  
																					No  becoz  print(hexa-decimal-number)  any  prints  decimal  equivalent		  																				
'''
