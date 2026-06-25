#  Find  outputs  (Home  work)
a =  [25]
#print(a[1]) # Error :  Index  1  does  not  exist  in  [25]
print(a[1:]) # List  without  first  element  i.e. []



'''
1) list[wrong-index]
    Is  it  valid / invalid ? ---> Invalid  due  to  wrong  index
	
2) list[wrong-index : wrong-index]
     Is  it  valid / invalid ? ---> Valid  but  the  result  is  []
	 
3) In  other  words,  indexing  	 raises  error  when  index  is  invalid  but  slicing  never  raises  error  even  when  indexes  are  invalid
'''
