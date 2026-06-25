'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''
a = input("Enter  any  mixed  case  string  :  ")  #   Reads  a  string
a = a . upper()  #   Returns  an  uppercase  string
out = ''
vowel = 'AEIOU'
for   ch   in   a: #   ch  is  each  char  of  the  string
        if   ch  in  vowel  and   ch  not  in  out:
                out += ch  #   Concatenates  the  character  to  object  out   if  it  is  vowel  and   not  in  object  out
print('Distinct  Vowels  :   ' , out)


'''
INPUT  :  RAMa  RAo
out  :
        ch      ch  in  vowel  and  ch  not  in  out                                            out
	-----------------------------------------------------------------------------------------
	  'R'       'R'  in  'AEIOU'  and  'R'  not  in  '' =  False                     out =  ''
	  'A'       'A'  in  'AEIOU'  and  'A'  not  in  '' =  True                     out = '' + 'A' = 'A'
	  'M'       'M'  in  'AEIOU'  and  'M'  not  in  'A' =  False                 out = 'A'
	  'A'       'A'  in  'AEIOU'  and  'A'  not  in  'A' =  False                  out = 'A'
	  ' '        ' '  in  'AEIOU'  and  ' '  not  in  'A' =  False                      out = 'A'
	  'R'        'R'  in  'AEIOU'  and  'R'  not  in  'A' =  False                  out = 'A'
	  'A'        'A'  in  'AEIOU'  and  'A'  not  in  'A' =  False                 out = 'A'
	  'O'        'O'  in  'AEIOU'  and  'O'  not  in  'A' =  True                 out = 'A' + 'O' = 'AO'
'''
