'''
Write  a  program  to  print  number  in  words

Let  input  be  123456789
What  is  the  output ?  --->  Tweleve  crores  thirty  four  lakhs  fifty  six  thousand  seven  hundred  eighty  nine

1) a = ['' , 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' ,   'Eleven' , 'Twelve' ,
           'Thirteen' , 'Fourteen' , 'Fifteen' , 'Sixteen' , 'Seventeen' ,  'Eightteen' , 'Nineteen']

2) b = [''  , '' , 'Twenty' , 'Thirty' , 'Forty' , 'Fifty' , 'Sixty' , 'Seventy' , 'Eighty' , 'Ninety']
            0     1          2              3            4             5           6              7               8               9

3) How  to  obtain  92  in  words ?  --->  b[92 // 10]  and  a[92 % 10]  = b[9]  and  a[2]
    How  to  obtain  50  in  words ?  --->   b[50 // 10]  and  a[50 % 10]  = b[5]  and  a[0]

4) How  to  obtain  14  in  words ?  --->  a[14]
    How  to  obtain  4  in  words ?  --->  a[4]

5) How  to  obtain  crores  part  from  123456789 ?  --->  123456789 // 10000000 = 12
    How  to  obtain  lakhs  part  from  123456789 ?  --->  123456789 // 100000 % 100 = 1234 % 100 = 34
    How  to  obtain  thousands  part  from  123456789 ?  --->  123456789 // 1000 % 100 = 123456 % 100 = 56
    How  to  obtain  hundreds  part  from  123456789 ?  ---> 123456789 // 100 % 10 = 1234567 % 10 = 7
    How  to  obtain  last  two  digits  of  the  number ?  ---> 123456789 % 100 = 89
'''
def  words(n , units):	 
	global  s	
	if  n >= 20:
		 s += b[n // 10] + ' ' + a[n % 10] + ' '  #   Concatenates  b[n // 10]  and  a[n % 10]  to  str  object  's'
	else:
		s += a[n] + ' '  #   Concatenates  a[n]  to  str  object  's'  when  n  is  below  20
	if  n > 0:
		s += units + ' '   #   Concatenates  units  to  str  object  's'  when  n  > 0
'''
1) words(92 , 'Crores')  --->  Ninety  two  crores

2) words(50 ,  'Lakhs')  --->  Fifty  Lakhs

3) words(14 , 'Thousand')  --->  Fourteen  Thousand

4) words(7 , 'Hundred')  ---> Seven  Hundred

5) words(0 , 'Crores')   --->  Nothing  becoz  1st  argument  is  0

6) Are  empty  strings  in  list  'b'  mandatory (or)  optional  ?  --->  Optional

7) What  modification  to  be  made  without  empty  strings  in  list  'b'  ?  ---> b[n // 10 - 2]

8) Is  empty  string  in  list  'a'  mandatory (or)  optional  ?  --->  Mandatory
'''
n = int(input('Enter any number (max : 999999999)  : ')) 
if  n == 0:
	print('Zero')
else:
	s = ''  #  Empty  string
	a = ['' , 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' , 'Eleven' , 'Twelve' , 
	        'Thirteen' , 'Fourteen' , 'Fifteen' , 'Sixteen' , 'Seventeen' , 'Eightteen' , 'Nineteen']  #   List  of  20  strings
	b = ['' , '' , 'Twenty' , 'Thirty' , 'Forty' , 'Fifty' , 'Sixty' , 'Seventy' , 'Eighty' , 'Ninety']  #   List  of  10  strings
	#     0    1         2              3            4            5            6               7              8              9
	words(n // 10000000 , 'crores')  #  Extracts  crores  part  from  the  input
	words(n // 100000 % 100 , 'lakhs')  #  Extracts  lakhs  part  from  the  input
	words(n // 1000 % 100 , 'thousand')  #  Extracts  thousands  part  from  the  input
	words(n // 100 % 10 , 'hundred') #  Extracts  hundreds  part  from  the  input
	words(n % 100 , '')  #  Extracts  last  two  digits  of  the  input
	print(s)  #  Prints  number  in  words
	

'''
1) Let  input  be  920017005
	What  is  the  result  of  920017005 / 10000000 ?  ---> 92
	What  is  the  result  of  920017005 / 100000 % 100 ?  --->  9200 % 100 = 0
	What  is  the  result  of  920017005 / 1000 % 100 ?  ---> 920017 % 100 = 17
	What  is  the  result  of  920017005 / 100 % 10 ?  ---> 9200170 % 10 = 0
	What  is  the  result  of  920017005 % 100 ?  ---> 5

2) Is  words(n % 100)  valid ?  --->  No  becoz  function  is  expecting  two  arguments  but  single  argument  is  passed
'''
