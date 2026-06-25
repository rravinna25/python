# Find outputs (Home work)
print(10 + 20) # 30
print(10.8 + 20.6) #  31.4
print(3 + 4j + 5 + 6j) # 8+10j
print(True + False) #  1 + 0 = 1
print('Hyder' + 'abad') # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma') #SankarDayalSarma
print('10' + '20') # 1020
print([10 , 20 , 30] + [1 , 2 , 3]) # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None)) # (25, 10.8, 'Hyd', (3+4j), True, None)
#print({10 , 20} + {30 , 40}) # Error : sets  cannot be concatenated  with  +  operator
#print({10 : 'Hyd'} + {20 : 'Sec'}) # Error : dictionaries cannot be concatenated  with  + operator
#print(range(4) + range(5))  # Error  :  range  objects  cannot be  concatenated
#print(10 + '20') # Error :  Operand2  should  be  a  non-sequence   as  operand1   is  a  non-sequence
#print([10 , 20 , 30] + 5) # Error :  Operand2  should  be  a  list  as  operand1  is  a  list  i.e.  List  and  int  can  not  be  concatenated
#print([10 , 20 , 30] + (40 , 50 , 60)) # Error  :  Operand2  should  be  a  list  as  operand1  is  a  list   i.e.  List  and  tuple  can  not  be  concatenated


'''
1) op1 + op2
   What  is  op2  of  +  operator  when  op1  is  a  non-sequence ?  ---> non-sequence
   
2) op1 + op2
    What  is  op2  of  +  operator  when  op1  is  a  list ?  ---> List
    What  is  op2  of  +  operator  when  op1  is  a  string ?  --->  string
    What  is  op2  of  +  operator  when  op1  is  a  tuple ?  --->  tuple
	
3) Can  sets  be  concatenated  with  +  operator ?  --->  No	
    Can  dictionaries  be  concatenated  with  +  operator ?  --->  No	
    Can  range  objects  be  concatenated ?  --->  No	
'''
