# Find outputs (Home work)
a = [10 , 20 , 30]
b = (10 , 20 , 30)
print(a  is  b) # False :  References  'a'  and 'b'  point  to  different  objects
print(a  ==  b) # False  :  References  'a'  and 'b'  point  to  different  objects


'''
1) [10 , 20 , 30] ==  (10 , 20 , 30)
    What  are  compared (objects / references) ?  --->									
											References  but  not  objects  even  though  ==  is  used  becoz  they  are  differnt  class  objects

2) [10 , 20 , 30] == [10 , 20 , 30]
    What  are  compared (objects / references) ?  --->  Objects  becoz  they  are  same  class  objects

3) 10 == 10.0
    What  are  compared (objects / references) ?  ---> Objects  becoz  they  are  non-sequences
'''
