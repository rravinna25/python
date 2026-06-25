'''
Let  input  be    VAMSI                         

Outputs   --->   V
					     VA
						 VAM
						 VAMS
						 VAMSI
'''
a = input('Enter  any  string  :  ');
print('Results')
for  i  in  range(1 , len(a) + 1):  #  Executes   loop  length  times
	print(a[:i])  #  String  of first  'i'  characters
	