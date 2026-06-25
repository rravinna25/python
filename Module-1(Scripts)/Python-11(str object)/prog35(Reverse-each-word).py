'''
Write  a  program  to  reverse  each  word  of  the  sentence

1) Let  input  be  Hyd  is  green  city
    What  is  the  output ?  ---> dyH si neerg ytic

2) Hint: Use  for  each  loop  and  also  slice
'''
a = input('Enter  any  sentence  :  ')
b = a . split()   # Divides  input  string  to  list  of  strings
c = ''
for  x   in   b:  #  'x'  is  each  string of  list  'b'
	c  +=  x[ : : -1]  + ' '  #   Reverses  each  string  of  list  'b'   and  concatenates  to  object  'c'  along  with  space
print(c)



'''
a = 'Hyd'
a += 'Hyd'
What  is  the  differenece  between  the  two  statements ?  --->  a = 'Hyd'  assigns  'Hyd'  to  object  'a'
																					                     but  a +=  'Hyd' concatenates  'Hyd'  to  object  'a'
'''
