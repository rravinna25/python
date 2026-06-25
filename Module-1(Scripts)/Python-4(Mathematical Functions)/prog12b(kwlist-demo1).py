# Find  outputs
from  keyword  import  kwlist
print(kwlist)  #  All  the  keywords  in  the  form  of  list  i.e. [True , False , None , and , or , not , in , is , if , else , yield , .....]
print(len(kwlist))  # Number  of  keywords  i.e.  35
print(type(kwlist))  #   <class  'list'>
#print(keyword . kwlist) # Error :  keyword  module  can  not be  used  as  it  is  is  not  imported 


'''
import  kwlist  
What  is  the  issue  ?  --->  import  statement  demands  module  but  kwlist  is  not  a  module
'''
