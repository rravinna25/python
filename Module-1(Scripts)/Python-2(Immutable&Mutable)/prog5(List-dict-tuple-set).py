 #Find  outputs(Home  work)
a = [10 , 20 , 15 , 18]   #  Ref   'a'  points  to  list
b = [10 , 20 , 15 , 18]  #  Ref 'b'  points  to  another  list  as   list  is  mutable  and  not  reusable
print(a  is  b) #  False  :  References  'a'  and  'b'  point  to  different  lists
c =  {10 : 20, 30 : 40}   #  Ref   'c'  points  to   dict
d =  {10 : 20, 30 : 40}  #  Ref 'd'  points  to  another  dictionary  as   dict  is  mutable  and  not  reusable
print(c  is  d)  #  False :  References  'c'  and  'd'  point  to  different  dictionaries
e = (10 , 20 , 15 , 18)    #  Ref   'e'  points  to   tuple
f = (10 , 20 , 15 , 18)  #  Ref 'f'  points  to  same   tuple  as  tuple  is  immutable  and  reusable
print(e  is  f)  #  True :  References  'e'  and  'f'  point  to  same  tuple
g = {10 , 20 , 15 , 18}    #  Ref   'g'  points  to   a   set
h = {10 , 20 , 15 , 18}   #  Ref 'h'  points  to  another  set   as   set  is  mutable  and  not  reusable
print(g  is  h)  #  False  :  References  'g'  and   'h'   point  to  different  sets
