'''
Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' ,  , 'Z' , 'K' ]

2) c = []

3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas']
                           c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                           c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''
a = eval(input('Enter  list  of  strings :  '))  #  Reads  a  list  of  strings
b = []  #  Empty  list
for  str  in  a:  #  str  is  each  string  of  list  'a'
	firstchar = str[0]  #  First  char  of each  string  in  list  'a'
	if  firstchar  not  in  b:
		b . append(firstchar)  #   Appends  first  char  to  list  'b'  if  it is  not in  list  'b'
# End  of  for  loop		
c = []  #  Empty  list
for  ch  in  b:  #  ch  is   each   char  of  list  'b'
	d = [] #  Empty  list
	for   str  in  a:    #  str  is  each  string  of  list  'a'
		if  str . startswith(ch):
			d . append(str)  #  Appends  the  string  to  list  'd'   if  it  starts  with  the  char  ch
	# End  of  inner  loop			
	c . append(d)    #   Appends   list 'd'  to  list  'c'
# End  of  outer  loop	
print(c)
