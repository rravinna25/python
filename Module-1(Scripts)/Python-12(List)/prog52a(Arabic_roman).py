'''
Write  a  program  to  convert  arabic  number  to   roman
1000 -  M
900 - CM
500 - D
400 - CD
100 - C
90 - XC
50 - L
40 - XL
10 - X
9 - IX
5 - V
4 - IV
1 - I

Input :  3878
Output :  MMMDCCCLXXVIII

1) str = ''	 
    n = 3878

2) x = 3878 // 1000 = 3
	str = '' + 'MMM' = 'MMM'
	n = 3878 % 1000 =  878

3) x = 878 // 900  = 0
	str = 'MMM'
	n = 878 % 900 =  878
 
4) x = 878 // 500 = 	1
    str = 'MMM' + 'D' = 'MMMD'
	n = 878 % 500 = 378
'''
n = int(input('Enter  number : '))
a = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]  #  List  of  arabic  numbers
b = ['M' , 'CM' , 'D' , 'CD' , 'C' , 'XC' , 'L' , 'XL' , 'X' , 'IX' , 'V' , 'IV' , 'I']  #  List  of  roman  numbers
s = ''  #   Empty  string
for i in range(len(a)):
    x = n // a[i]  #  Number  of   a[i]'s  in  the  input
    s +=  b[i] * x  #   Concatenate  'x'   b[i]'s  to  the  result
    n = n % a[i]  #  Modifies  'n'  
# End  of  the  for  loop	
print('Roman  number  :  ' ,  s)  #   Result
