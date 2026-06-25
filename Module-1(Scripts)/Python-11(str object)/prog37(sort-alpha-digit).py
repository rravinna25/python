'''
Write  a  program  to  sort  string  such  that  alphabets  in  alphabetical  order  and  digits  in  ascending  order

Let  input  be  Z9K3PA7D51
What  is  the  output ?  --->  ADKPZ13579

1)What  is  the  result  after  input  is  sorted ?  --->  '13579ADKPZ'

2) alpha = '' + 'A' + 'D' + 'K' + 'P' + 'Z'
    digit = '' + '1' + '3' + '5' + '7' + '9'

3) What  is  the  result  after  alpha  and  digit  are  concatenated ?  --->  'ADKPZ13579'
'''
a = input('Enter  string  with  alphabets  and  digits  :  ')
b = sorted(a)  #  Sorts  chars  of  input  string  to  form  a  list  of  sorted  chars
alpha = digit = ''  #  Empty  string
for  ch   in   b:  #  ch  is  each  char  of  list  'b'
	if  ch . isalpha():
		alpha  += ch  #  Concatenates  the  char  to  object  alpha  if  it  is  an  alphabet
	elif  ch . isdigit():
		digit  += ch  #  Concatenates  the  char  to  object   digit  if  it  is  a  digit
# End  of  for  loop
print('Result  :  ' ,  alpha + digit)
