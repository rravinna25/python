#  Find  outputs  (Home  work)
r = range(10 ,  17 , 3)  #Object  contains  elements  from  10  to  16  in  steps  of  3
a , b , c = r  #  Unpacks  range  object  to  3  elements
print(a , b , c) #  10 <space>  13  <space>  16
r = range(3)   #Object  contains  elements  from   0   to  2   in  steps  of  1
#x , y = r   #   Error :  Excess  elements  in  range  object
#p , q  , r , s = r  #  Error :   Few  elements  in  range  object
#a , b , c = *r  #  Error  due  to  *  operator
m = r  #  Ref  'm'  points  to  object  'r'
print(id(r))  #   Address  of  range  object  'm'
print(id(m))  # Same  address


'''
x , y , z = range-object
x = range-object
What  is  the  difference  between  the  two  statements ?  --->  1st  statement  unpacks  the  range   object  to  3  elements  
																												and
																									   2nd  statement  assigns  ref  'x'  to  the  range  object
'''
