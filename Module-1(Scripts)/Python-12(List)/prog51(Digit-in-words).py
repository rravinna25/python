'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Input : 9247
Output :  Nine  Two  Four  Seven
'''
list = ['Zero' , 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine']  #  List  of  10  strings
#          0           1           2           3            4          5         6           7           8             9
str = input('Enter  any  number  :  ')  #  Reads  number  in  the  form  of  string
out = ''  #   Empty  string
for  ch  in   str:  #   ch  is  each  digit  of  the  string  number
		digit = int(ch)  #  Converts  each  char  to  digit
		out += list[digit] + ' '  #  Concatenates  appropriate  string  in  the  list  to  str  object  out
print(out)		
