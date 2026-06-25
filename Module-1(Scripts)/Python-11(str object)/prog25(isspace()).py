# isspace()  method  demo  program  (Home  work)
print('\n  A\t' . isspace())  #  False  due  to   'A'
print('\n  \t' . isspace()) #  True :  Every  char  of  '\n  \t'  is  whitespace
print('\n  7\t' . isspace())  #  False  due  to   '7'
print('\n' . isspace())   #  True :  Every  char  of  '\n'  is  whitespace
print('\n  $\t' . isspace())  #  False  due  to   '$'
print('\t' . isspace())   #  True :  Every  char  of  '\t'  is  whitespace
print('' . isspace())   #  False  due  to   no  white  spaces  in  ''
print(' ' . isspace())     #  True :  Every  char  of  ' '  is  whitespace



'''
isspace()  method
---------------------
1) When  does  it  return  True ?  --->  When  every  character  of  the  string  is  white  space  character

2) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  not  a  white  space
                                                               i.e.  Alphabet, digit (or)  special  character
'''
