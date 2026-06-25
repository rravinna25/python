 # Find  outputs
def   f1(a = 'Hyd' , b = []):
	a += "Sec"
	b +=  [1 , 2 , 3]
	print('a :  ' , a)
	print('b :  ' , b)
# End of the function
print('Default Values  :  ' , f1 . __defaults__) # Default Values  : ('Hyd' , [])
f1() # 'a'  is   default  value  'Hyd' ,  'b'  is  default  value  []  and  result  is  a : HydSec <next line> b : [1 , 2 , 3]
print('Default Values  :  ' , f1 . __defaults__) # Default Values  :  ('Hyd' , [1 , 2 , 3])
f1() # 'a'  is   default  value  'Hyd' ,  'b'  is  default  value  [1 , 2 , 3]  and  result  is  a : HydSec <next line> b : [1 , 2 , 3 , 1 , 2 , 3]
print('Default Values  :  ' , f1 . __defaults__) # Default Values  :  ('Hyd' , [1 , 2 , 3 , 1 , 2 , 3])
f1() # 'a'  is   default  value  'Hyd' ,  'b'  is  default  value  [1 , 2 , 3 , 1 , 2 , 3]  and  result  is  a : HydSec <next line> b :  [1 , 2 , 3 , 1 , 2 , 3 , 1 , 2 , 3]


'''
1) When  is  __defaults__ modified ?  --->  When  function  modifies  mutable  default  argument  such  as  list

2) When  is   __defaults__  unchanged ?  --->  When  function  modifies  immutable  default  argument  such  as  string

3) a = 'Hyd'
    a += 'Sec'
    What  is  modified  (reference  (or)  object) ?  --->  Reference  'a'  but  not  str  object  as  it  is  immutable

4) b = [1 , 2 , 3]
    b += [1 , 2 , 3]
    What  is  modified  (reference  (or)  object) ?  ---> Object  becoz  list  is  mutable
'''
