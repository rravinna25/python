# copy()  method demo  program  (Home  work)
a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
b = a . copy()  #  Copies  all  the  key : value  pairs  of  dict  'a'  to  'b'
print(b) # {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
print(a  is  b) # False  : References  'a'  and  'b'  point  to  different  dictionaries
print(a  ==  b) # True :  Same  key  value  pairs  in  dictionaries   'a'  and  'b'


'''
1) What  is  another  way  to  copy  dictionary  'a'  to  'b'  ?  --->  b = {**a}

2) a = {'R' : 'Red' , 'G' : 'Green' , 'B' : 'Blue'}
    What  is  the  issue  with  b = {a}  ?  --->  Set  can  not  have  mutable  element  suct  as  dictionary
'''
