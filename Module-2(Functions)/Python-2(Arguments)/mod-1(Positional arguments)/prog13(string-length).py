# Write  a  function  for  string  length  without  using  len()  function
def  length(a):
	ctr = 0
	for  ch   in  a:  #  ch  is  each  char  of  the  string
			ctr += 1  #  Counts  each   char  of  the  string
	# End  of  for  loop				
	return  ctr #  Number  of  chars  in  the  string
# length('RAMA')  --->  4
a = input('Enter any string :  ')	
print('String  Length  :  ' ,   length(a))
