# isdigit()  method  demo  program  (Home  work)
print('9247' . isdigit())  #  True :  Every  char  of  '9247'  is  a  digit
print('92a47' . isdigit()) #  False  due  to  'a'
print('92$47' . isdigit()) #  False  due  to  '$'
print('Hyd' . isdigit())  #  False  due  to  'H'
print('+-$' . isdigit())  #  False  due  to  '+'
print('A2#' . isdigit())  #  False  due  to  'A'
print('' . isdigit())  #  False :  No  digits  in  the  string
print(' ' . isdigit())  #  False  due  to  ' '
#print(9247 . isdigit())  #  Error :  int  class  does  not  have  isdigit()  method  


'''
isdigit()  method
--------------------
1) When  does  the  method  return  True  ?  --->  When  every  character  of  the  string  is  a  digit

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  non-digit(i.e. alphabet  (or) special  character)
																					   (or)
															  When  there  are  no  digits  in  the  string
'''
