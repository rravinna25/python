'''
Write  a  function  for  duplicate  largest.

Function  should  return  a  list  consisting  of   indexes  of  each  largest  element
Use  the  function  to  print  number  of  times  largest  element  is  found  in  the  list

Assume  that  largest  element  is  present  at  multiple  locations  of  list

Input  List :  [10 , 20 , 30 , 25 , 18 , 30 , 19 , 18 , 30 , 25]
			           0     1     2     3    4     5     6    7     8     9

What  are  the  outputs  ?  --->   List  of  indexes  of  largest  element  : [2 , 5 , 8]
													Number  of  times  largest  element  is  repeated :  3
'''
def  duplar(a):
	large = max(a)	
	b = []		
	i = -1
	while  True:
			try:
				i = a . index(large , i + 1)
				b . append(i)
			except:
				return  b
# End  of  the	 function
a = eval(input('Enter  list  with  duplicate  largest  elements :  '))
c = duplar(a)
print('List  of  indexes  of  largest  element :  ' , c)
print(F'Largest  element  {max(a)}  is  found  {len(c)}  times')
