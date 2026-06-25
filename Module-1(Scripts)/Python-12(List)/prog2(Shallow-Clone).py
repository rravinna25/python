#  Find  outputs (Home  work)
a = [10, 20, 15, 18]
b = a  # 'b'  points  to  list  'a'
print(a  is  b) # True :  References  'a' and  'b'  point  to  same  list
print(a  ==  b) # True : Elements  of  lists  'a'  and  'b'  are same
b[2] = 12  # Modifying  list  'b'  is  as  good  as  modifying  list  'a'
print(a) #  Modified   list  i.e. [10, 20, 12, 18]


'''
1) What  is  shallow  clone ?  --->  Reference  copy  but  not  object  copy

2) What  does  b = a   do  ? --->  Shallow  clone

3) In  other  words,  b = a  assigns  reference  'b'  to  list  'a'

4) Finally  b = a  does  not  copy  elements  of  list  'a'  to  list  'b'

5) How  many  lists  are  in  the  above  program ?  --->  Single  list  with  two  references   a  and  b

6) b[2] = 12
    Modifying  list  'b'  is  as   good  as  modifying  list  'a'  becoz  'a'  and  'b'  point  to  same  list
'''
