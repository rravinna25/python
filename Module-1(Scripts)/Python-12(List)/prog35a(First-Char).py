'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension

Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a = eval(input('Enter  list  of  lower  case  strings :  '))  #  Reads  list  of  strings
b = []  #  Empty  list
for  x  in  a:  #  'x'  is  each  string   of  list  'a'
	b . append(x[0] . upper())  #  Appends  1st  char  of  string  'x'  in  uppercase  to  list 'b'
print(b)


'''
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
1) What  is  list  'a'  ?  --->  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

2)    x                         x[0]                               x[0] . upper()           List  'b'
    ------------------------------------------------------------------------------------------
                                                                                                                []
        'hyd'                 'hyd'[0]  is  'h'              'h' . upper()  is  'H'        ['H']
        'pune'               'pune'[0]  is  'p'             'p' . upper()  is  'P'         ['H' , 'P']
        'chennai'          'chennai'[0]  is  'c'         'c' . upper()  is  'C'         ['H' , 'P' , 'C']
        'vijayawada'     'vijayawada'[0]  is  'v'    'v' . upper()  is  'V'         ['H' , 'P' , 'C' , 'V']
'''
