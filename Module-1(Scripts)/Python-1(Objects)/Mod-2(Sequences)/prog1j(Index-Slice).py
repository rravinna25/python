#  Find  outputs  (Home  work)
a =  'A'
#print(a[1]) #  Error  becoz  index 1  does  not  exist  in  'A'
print(a[1:]) # String  without   1st   char  i.e.  ''



'''
1) string[invalid-index]
    Is  it  valid / invalid ?  --->  Invalid  due  to  invalid  index

2) string[invalid-index : invalid-index]
    Is  it  valid / invalid ?  --->  Valid  but  the  result  is  empty  string
	
3) In  other  words,  indexing  raises  error  when  the  index  is  invalid  but
    slicing  never  raises  error  even  when  indexes  are  invalid
'''
