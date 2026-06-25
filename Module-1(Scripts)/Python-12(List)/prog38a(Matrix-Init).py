'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''
m = int(input('How  many  lists  ?  :  '))
n = int(input('How  many  elements  in  each  list ?  :  '))
a = []
for  i  in   range(m):   #  Appends  'm'  lists  to  list  'a'
	a .  append([0] * n)  #  Appends  list  of  'n'  zeroes  to  list  'a'
print(a)


'''
m --->  3
n  --->  4
      i          [0] * n                                 list  a
 ---------------------------------------------------------------------------
		 													     []
   	  0          [0] * 4 = [0 , 0 , 0 , 0]          [[0 , 0 , 0 , 0]]
      1          [0] * 4 = [0 , 0 , 0 , 0]          [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
      2          [0] * 4 = [0 , 0 , 0 , 0]          [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

1) What  is  the  result  of  0 * 4 ?  ---> 0

2) What  is  the  result  of  [0] * 4  ? ---> [0 , 0 , 0 , 0]

3) a = []
    for  i  in   range(3):
	       a . append(0 * 5)
    print(a)
    What  is  printed ?  ---> List  of  3 zeroes
	
4) a = []
    for  i  in   range(3):
	       a . extend([0] * 5)
    print(a)
	What  is  printed ?  ---> List  of  15  zeroes
'''
