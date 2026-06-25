'''
Tricky  program
Write  a  program  to  remove  all  duplicate  elements  of  the  list  (Not  even  single  occurance)
Let  input  be  [10 , 20 , 15 , 10 , 14 , 10 , 18 , 20 , 19]
What  is  the  output ?  ---> [15 , 14 , 18 , 19]

Hint:  Use  count()  and  append()  methods
'''
a = eval(input('Enter  List :  '))  #  Reads  list
b = []  #  Empty  list
for  x  in   a:  #  'x'  is  each  element  of  list  'a'
	if a . count(x) == 1:
		b . append(x)  #  Appends  'x'  to  list  'b'  if  'x'  is  found  in  list  'a'  just  once
print(b)


'''
1) for  x  in   a:
	     if a . count(x) == 1:
		       b . append(x)
    What  is  the  issue  when  list  'a'  is  not  converted  to  set ?  --->  Execution  becomes  slow
																											    i.e. Processor  time  is  wasted

2) In  other  words,  number  of  iterations  are  increased
																												
3) for  x  in  set(a):
		if a . count(x) == 1:
	 	          b . append(x)
     What  is  the  advantage  of  converting  list  'a'  to  set ?  --->  Execution  becomes  faster
	 
4) In  other  words,  number  of  iterations  are  reduced
'''
