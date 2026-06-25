# Write  a  function  to  concatenate  strings  passed  to  the  function   ? (Home  work)
def  concat(*a):  #  'a'  is  tuple  of  strings  passed  from  the  function  call
    return  ' ' . join(a) #   Joins  strings  in  tuple  'a'  with  space  to  form  a  string
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma')) #  Sankar<space>Dayal<space>Sarma  :  Tuple  of  3  strings  is  passed  to  the   method  
print(concat('Hyd', 'Is', 'Green', 'City')) #  Hyd<space> Is <space>Green <space>City  : Tuple  of  4   strings  is  passed  to  the   method  
print(concat('Python', 'Is', 'A', 'Great', 'Language')) #  Pyhton<space>Is<space>A<space>Great<space>Language  : Tuple  of  5  strings  is  passed  to  the   method 
print(concat()) #  Nothing :  Empty  Tuple  is  passed  to  the   method  i.e. Empty string
print(concat('Python')) #  Python : Tuple  of  1  string  is  passed  to  the   method  
#print(concat(1, 2, 3)) # Error :  Tuple  of  3  integers  is  passed  to  the   method   but  tuple  of  integers  can not  be   joined


'''
a = (1 , 2 , 3)
What  is  the  issue   with  ' ' . join(a)  ?  --->  Can  not  join  tuple  of  integers
'''
