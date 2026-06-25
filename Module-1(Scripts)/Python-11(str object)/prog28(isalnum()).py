# isalnum()  method  demo  program  (Home  work)
print('A7$g'  . isalnum()) #  False  due  to   '$'
print('HYD' . isalnum()) #  True  :  No  special  chars  in  'HYD'
print('+-$' . isalnum())  #  False  due  to   '+'
print('hyd' . isalnum())  #  True  :  No  special  chars  in  'hyd'
print('hYd' . isalnum())   #  True  :  No  special  chars  in  'hYd'
print('9247' . isalnum())  #  True  :  No  special  chars  in  '9247'
print('' . isalnum())   #  False :  No  alphabets   nor   digits  in   ''
print('A7g9'  . isalnum())  #  True  :  No  special  chars  in  'A7g9'


'''
isalnum()  method
----------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  speical  character
																						(or)
															  when  there  are  no  alphabets  (or)  digits

2) When  does  it  return  True ?  --->  When  there  are  no  special  characters  in  the  string

3) What  is  isalpha()  +  isdigit()  called ?  --->  isalnum()
'''
