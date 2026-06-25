# islower()  method  demo  program  (Home  work)
print('hyD' . islower())  #   False  due  to  'D'
print('hyd' . islower())  #  True :  No  uppercase  alphabets  in  'hyd'
print('9247' . islower())  #  False :  No  lowercase  alphabets  in   '9247'
print('rama  rao' . islower())   #  True :  No  uppercase  alphabets  in  'rama rao'
print('+-$' . islower())  #  False :  No  lowercase  alphabets  in   '+-$'
print('hyd+-$' . islower())  #  True :  No  uppercase  alphabets  in  'hyd+-$'
print('abc123' . islower())  #  True :  No  uppercase  alphabets  in  'abc123'
print('' . islower())   #  False :  No  lowercase  alphabets  in   ''
print('a2#' . islower())   #  True :  No  uppercase  alphabets  in  'a2#'


'''
islower()  method
---------------------
1) When  does  it  return  False ?  --->  When  at  least  one  character  of  the  string  is  uppercase  alphabet
																								(or)
															 When  there  are  no  lowercase  alphabets  in  the  string

2) When  does  it  return  True ?  --->  When  there  are  no  uppercase  alphabets  in  the  string
																						and
															 at  least  one  character  is  an  lowercase  alphabet

Note:
1) What  are  upper()  and  lower()  called ?  ---> Conversion  methods

2) What  are  isupper()  and  islower()  called ?  --->  Conditional  methods  becoz  they  return  True  (or)  False
'''
