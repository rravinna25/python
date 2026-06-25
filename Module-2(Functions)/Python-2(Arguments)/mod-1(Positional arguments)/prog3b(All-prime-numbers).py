'''
Write  a  function  to  return  list  of  all  the  prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Reuse  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers  :  [2 , 3 , 5 , 7]																		   
																		   Number  of   prime  numbers : 4
'''
from  prog3a   import  prime   #  Imports  prime()  function  and  the  if  statement  from  prog3a
def  all_prime_numbers(n):
	list = []  #  Empty  list
	for  i  in   range(2 , n + 1):  #   Prime  numbers  between  2  and  n
		if  prime(i):
			list . append(i)	  #  Appends  'i'  to  the  list  if  'i'  is  prime  number
	#  End  of  for  loop		
	return  list  #  Returns  List  of  all  prime  numbers  to  the  function  calll
# End  of  the  function	
n = int(input("Enter  value  of  'n' :  "))    #   Reads  input
a = all_prime_numbers(n)  #  Ref  'a'  points  to  the  list  returned  by  the  function
print('Prime numbers  :  ' ,  a)  #   List  of  prime  numbers
print('Number  of  prime numbers  :  ' ,   len(a))  


'''
1) py   prog3a.py
    What  is  the  value  of  __name__  varaible ?  --->  '__main__'

2) import  prog3a
    What  is  the  value  of  __name__  varaible ?  --->  'prog3a'

3) from  prog3a  import  prime
     What  is  the  value  of  __name__  varaible ?  --->  'prog3a'
	 
4) if  statement  is  imported  from  prog3a  but  not  executed  becoz  condition  is  False
'''
