'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
for  ch  in  range(65 , 91):
	print(chr(ch) , end = '  ')  #  Prints  chr(ch)  where  ch  varies  from   65  to  90
print()
for  ch  in  range(97 , 122):
	print(chr(ch) , end = '  ')	#  Prints  chr(ch)  where  ch  varies  from   97  to  122
print()
