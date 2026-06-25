''''
Gift

Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->   14.5

Hint:  Use  while  loop

Iteration         a          op        b        result
------------------------------------------------------
      1                3          +          4            7       
      
	  2               7           *         5            35
	  
	  3               35         -          6            29
	  
	  4               29         /          2            14.5
	  
	  5               14.5      =          ----         ----
'''
str = input('Enter  any  expression  terminated  by  =  :  ')  #  3 + 4 * 5 - 6 / 2 =
a = eval(str[0]) 
op = str[1]
i = 2
while  op  !=  '=':	
	b = eval(str[i])  
	match  op:        
		case '+':  
				a += b                           
		case '-':  
				a -= b                           
		case '*':  
				a *= b                           
		case '/':  
				a /= b
	# End  of  match                    
	i += 1 
	op = str[i]  
	i += 1  
#  End  of  while  loop    
print('Result : ' , a)


'''
1) Where  is  operand1  stored  ?  --->   In  object  'a'
    Where  is  operator  stored ?  --->  In  object  op
    Where  is  operand2  stored ?  ---> In  object  'b'

2) Do  not  press  space  bar  (or)  tab  key  in  the  expression  becoz  it  is  a  calculator  simualtion

3) Use  single  digit  operands
'''
