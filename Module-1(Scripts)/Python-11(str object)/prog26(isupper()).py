# isupper()  method  demo  program  (Home  work)
print('HYd' . isupper())  #  False  due  to  'd'
print('HYD' . isupper()) #  True  :  No  lowercase  alphabets  in 'HYD'
print('9247' . isupper()) #  False :  No  uppercase  alphabets  in  '9247'
print('RAMA  RAO' . isupper())  #  True  :  No  lowercase  alphabets  in  'RAMA RAO'
print('+-$' . isupper())  #  False :  No  uppercase  alphabets  in  '+-$'
print('HYD123' . isupper())  #  True  :  No  lowercase  alphabets  in 'HYD123'
print('HYD+-$' . isupper())  #  True  :  No  lowercase  alphabets  in 'HYD+-$'
print('' . isupper())    #  False :  No  uppercase  alphabets  in  ''
print('A2#' . isupper())  #  True  :  No  lowercase  alphabets  in  'A2#'


'''
isupper()  method
----------------------
1) When  does  the  method  return  False ?  --->  When  at  least  one  character  of  the  string  is  lowercase  alphabet
																								(or)
															                   When  there  are  no  uppercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  lowercase  alphabets  in  the  string
																						and
															  at  least  one  character  is  an  uppercase  alphabet
'''
