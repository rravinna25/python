'''
Write  a  function  to  test  a  string  is  palindrome  (or)  not

What  is  a  palindrome  string  ?  --->  Reverse  string  and  input  string  should  be  same
'''
def  palin(a):
	return   a == a[::-1]  #  True  when  input  string  and  reverse  string  are  same  and  False  otherwise
'''	
1) palin('RAMA')  --->  False

2) palin('MADAM')  ---> True
'''
a = input('Enter  any  string  :  ')  #  Reads  input  string
if  palin(a):  #  Is  string  'a'  palindrime  ?
	print('Palindrome')
else:
	print('Not  Palindrome')
