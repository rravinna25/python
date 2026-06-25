#  isalpha()  method  demo  program (Home  work)
print('Hyd'  . isalpha())  #  True :  Every  char  of  'Hyd'  is  an  alphabet
print('Rama  Rao'  . isalpha())  #  False  due  to  space
print('Hyd4'  . isalpha())   #  False  due  to   '4'
print('Hyd$'  . isalpha())   #  False  due  to  '$'
print('9247'  .  isalpha())   #  False  due  to   '9'
print('+-$'    .  isalpha())   #  False  due  to  '+'
print('A2#'  .   isalpha())    #  False  due  to   '2'
print(''  .  isalpha())   #  False :  No  alphabet
print(' '  .  isalpha())   #  False  due  to   space


'''
isalpha()  method
---------------------
1) When  does  the  method  return  True ? --->  When  every  character  of  the  string  is  alphabet

2) When  does  it  return  False  ?  ---> When  at  least  one  character  of  the  string  is  non-alphabet(i.e. digit (or) special  character)
																					    (or)
															  When  there  are  no  alphabets  in  the  string
'''
