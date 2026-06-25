'''
Write  a   function  to  return  the  char  which  is  repeated  max  number  of   times

Input  :  RAMA RAO

How  many  R's  are  in  the  string ?  --->  2
How  many  A's  are  in  the  string ?  --->  3
How  many  M's  are  in  the  string ?  ---> 1
How  many  spaces  are  in  the  string ?  --->  1
How  many  O's  are  in  the  string ?  ---> 1

ctr = 3
mode = 'A'
What  is  the   result ?  --->  A
'''
def  mode_char(a):  #  'a'  is   Rravinna Reddy
	ctr = 0
	a = a . upper()
	for  ch  in  a: #  ch  is  each  char  of  the  string
		freq = a . count(ch) #   Number  of  times  ch  is  in  the  string
		if  freq >= ctr: #  Is  freq  >  ctr
			ctr = freq  #  Modifies  ctr
			mode = ch #  Modifies  mode
	# End  of  for  loop
	return  mode  #  The  first  char  which  is  repeated  max  number  of   times
# End  of  the  function
a = input('Enter  any  string :  ')
print('The  char  which  is  repeated  max  number  of  times  :  ' , mode_char(a))
