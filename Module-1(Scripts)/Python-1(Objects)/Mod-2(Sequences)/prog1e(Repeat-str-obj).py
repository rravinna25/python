#  Find  outputs  (Home work)
a = 'Hyd'  #  Ref  'a'  points  to  object   'Hyd'
print(a , id(a))  #  Hyd   <space>  Address  of  'Hyd'
a = a * 3  #  Modifies  ref   'a'  to  a  new  string   object 'HydHydHyd'
print(a , id(a))  #  HydHydHyd    <space>   Address


'''
1) a = 'Hyd'
    a = a * 3
	Is  reference  modified  (or)  object ?  --->  Reference
	
2) a = 'Hyd'
    a = a * 3
	Where  does  ref  'a'  points  to  ?  --->  New  string  'HydHydHyd'

3) a = 'Hyd'
    a = a * 3
	Why  is  object  not  modified ?  --->  Since  str  object  is  immutable
'''
