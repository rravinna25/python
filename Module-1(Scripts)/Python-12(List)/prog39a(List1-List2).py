'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''
a = eval(input('Enter 1st  list  :  ')) #   Reads  1st  list
b = eval(input('Enter 2nd  list  :  '))  #   Reads  2nd  list
c = []  #  Empty  list
for  x  in   a:  #  'x'  is  each  element  of  list  'a'
	if  x  not  in  b:
		c . append(x)  #   Appends  'x'  to list  'c'  if  it  is  not in list  'b'
print('Elements  of  1st  list  which  are  not  in  2nd  list  :  ' , c)



'''
List   'a'  --->  [10 , 20 , 15 , 18 , 25 , 32]
List   'b'  --->  [30 , 40 , 10 , 25 , 15]

 x         x  not  in   b      List  'c'
---------------------------------------------------
                                         []
 10           False                 []
 20          True                  [20]
 15           False                 [20]
 18           True                  [20 , 18]
 25           False                 [20 , 18]
 32           True                 [20 , 18 , 32]
 
 
1) a = []
    a . extend(25)
	Is   the  statement  valid ?  --->  No  becoz  extend()  method  expects  sequence  but  25  is  not  a  sequence
	
2) a = []
    a . append(25)
	Is   the  statement  valid ?  --->   Yes  becoz  append()  method  takes  any  python  object
'''
