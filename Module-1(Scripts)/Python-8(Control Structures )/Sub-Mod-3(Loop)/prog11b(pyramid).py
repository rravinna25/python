'''
Write  a  program  to  print
        A
      A B
     A B C
   A B C D
A B C D E
 
Input  is  number  of  lines
Hint:  chr(65) = 'A'	
          chr(66) = 'B'	
          chr(67) = 'C'	
	       .....
	       chr(90) = 'Z'
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character		   
'''
n = int(input("Enter number of lines: "))  
s = n - 1   #   Number  of  spaces  in  1st  line
for i in range(1, n + 1):  #   Print  'n'  lines
    print(' ' * s, end='')    #   Prints  's'  spaces
    for j in range(i):     
        print(chr(65 +j), end=' ')  #  Prints  alphabets
    print()  #  Moves  to  next  line
    s -= 1   #  Decrement  number  of  spaces  by  1
	