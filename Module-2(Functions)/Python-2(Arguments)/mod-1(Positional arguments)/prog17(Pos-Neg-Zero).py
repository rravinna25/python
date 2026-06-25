'''
Write  a  function  to  return  a  list  of  +ve  values , -ve  values  and  0's  in  a  list

					     
Input  list --->  [-10 , 20 , 0 , -40 , 0 , 50 , -60]
						
Output  list  --->	[2 , 3 , 2]
'''				        
def  count(a):
	p = n = z = 0
	for  x  in  a:
		if  x > 0:
			p += 1  #  Counts  number  of  +ve  elements  in  the  list
		elif  x < 0:
			n += 1   #  Counts  number  of  -ve  elements  in  the  list
		else:
			z += 1  #  Counts  number  of   zeroes in  the  list
	# End  of  for  loop			
	b = [p , n , z] #  Packs  3  objects  to  form  a  list
	return  b
# End  of  the  function	
a = eval(input('Enter  list  of  +ve  elements , -ve  elements  and  zeroes  :  '))
c = count(a)
print('Number  of  +ve  elements : ' , c[0])
print('Number  of  -ve  elements : ' , c[1])
print('Number  of  zeroes : ' , c[2])
