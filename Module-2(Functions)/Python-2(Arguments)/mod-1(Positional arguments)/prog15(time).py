'''
Write  a  function  to  convert  time  string  into  seconds

1) Let  input  be  15 : 38 : 46
   What  is  the  output ? ---> 15 * 3600 + 38 * 60 + 46

2) What  is  the  range  of  hours ?  --->  0  to  23
    What  is  the  range  of  minutes ? ---> 0  to  59
    What  is  the  range  of  seconds ?  ---> 0  to  59
'''
def  eval(a):    	
	list = a . split(':')  #  Splits  time  string  into  list  of  3  strings
	h , m , s = list  #  Unpacks  list  into  3  elements
	h , m , s =   int(h) , int(m) , int(s)	 #  Converts  hours , minutes  and  second  to  integers
	while  h < 0  or  h > 23  or  m < 0 or  m > 59  or  s < 0  or  s > 59:  #  Execute  loop  until  user  types  valid  time
		a = input('Invalid  time  ,  reenter :  ')  
		list = a . split(':')  #  Splits  time  string  into  list  of  3  strings
		h , m , s = list  #  Unpacks  list  into  3  elements		
		h , m , s =   int(h) , int(m) , int(s)	 #  Converts  hours , minutes  and  second  to  integers
	# End  of  while  loop
	return  h * 3600 + m * 60 + s  #   Converts  hours , minutes  and  seconds  to  seconds
'''
1) eval('15:48:35')  --->  15 * 3600 +  48 * 60 + 35

2) Can  while  loop  be  replaced  with  'if'  in  eval()  function ?  --->
																		No  becoz  new  time  is  not  validated  as  'if'  is  one  time  execution

3) What  is  the  advantage  of  while  loop ?  ---> It  enforces  user  to  type  a  valid  time
'''
a = input('Enter time in the format  hh : mi : ss  ---> ')
print('Equivalent   Seconds  :  ' ,  eval(a))


'''
Which  of  the  following  are  valid  inputs ?
1) 07 : 08 : 09  ---> Valid

2) 7 : 8 : 9  ---> Valid
'''
