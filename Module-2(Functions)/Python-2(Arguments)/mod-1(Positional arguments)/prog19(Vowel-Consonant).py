'''
Write   a  program  to  count  number  of   characters , words ,  spaces , tabs , sentences , vowels  and  consonants  in  a   string


Input :  Rama Rao

List  'a'  --->   [8              2            1              0             0                 4                3] 
                       Chars     Words   Spaces     Tabs     sentences    Vowels     Consonants
'''
def  count_all(str):	
	words = str . split()  
	a = [len(str) ,  len(words) , str . count(' ') , str . count('\t') , str . count('.')]
	vowel = 'AEIOUaeiou'
	v = c = 0
	for   ch  in  str:  
		if  ch  in   vowel:
				v += 1   
		elif  ch . isalpha():
				c += 1  
	#  End  of  for  loop				
	a += [v , c]
	return  a
#  End  of   function
str = input('Enter  a  string :  ')
b = count_all(str)
c = ['Chars' , 'Words' , 'Spaces' , 'Tabs' , 'Sentences' , 'Vowels' , 'Consonants']
for  i  in   range(len(c)): 
		print(c[i] , b[i] , sep = '...')		


'''
for  i  in   range(len(b)): 
		print(b[i])
What  is  the  issue  if  only  b[i]  is  not  printed ?  --->  Outputs  will  not  have  clarity
'''
