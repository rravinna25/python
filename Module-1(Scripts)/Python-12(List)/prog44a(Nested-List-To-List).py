'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a = eval(input("Enter nested list : ")) #  Reads  a  nested  list
b = []  #  Empty list
for  x  in  a:   #  'x'  is  each  inner  list   of  list  'a'
	b . extend(x)  #  Appends  elements  of  list  'x'  to  list  'b'
print(b)


'''
Iteration         x                         b . extend(x)
---------------------------------------------------------------									
      1             [10 , 20]                    [10 , 20]
      
	  2            [30 , 40 , 50]              [10 , 20 , 30 , 40 , 50]
	  
	  3            [60 , 70 , 80 , 90]       [10 , 20 , 30 , 40 , 50 ,  60 , 70 , 80 , 90]
'''	  