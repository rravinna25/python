'''
Write  a  program  to  convert  roman  number  to  arabic  number
 
1) Input :  VIII
   Output :  8
   Reverse  input :  IIIV
   prev = 5
   sum = 0 + 1 + 1 + 1 + 5 = 8
2) Input :  IX
    Output :  0
    Reverse  input :  XI
	prev = 1
	sum = 0  + 10  - 1 = 9
3) Input : MMMDCCCLXXVIII
    Reverse  input :   IIIVXXLCCCDMMM
	prev = 1000
	sum = 0  + 1 + 1 + 1 + 5 + 10 + 10 + 50 + 100 + 100 + 100 + 500 + 1000 + 1000 + 1000
'''
roman = input("Enter Roman Number : ")  #   MMMCMCCCXCXXIXIII
a = {'I' : 1 , 'V' : 5 ,  'X' : 10 , 'L' :  50 , 'C'  : 100 , 'D' :  500 , 'M' : 1000}
s = 0
prev = 0
for ch in roman[::-1]:  #   IIIXIXXCXCCCMCMMM
	x = a[ch]  #  x = 100
	if x >= prev:
		s += x
	else:
		s -= x
	prev = x
print("Arabic Number =", s)  
