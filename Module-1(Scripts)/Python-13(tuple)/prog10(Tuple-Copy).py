# How  to  copy  tuple ?   (Home  work)
a = (10 , 20 , 15 , 18)
print(id(a)) #  Address  of  tuple  (10 , 20 , 15  , 18)
#b = a . copy()  #  Error :  No  copy()  method  in  tuple
b = tuple(list(a))  #  Converts  tuple   to  list  and  list  to  tuple  ,  Ref  'b'  points  to  a  new  tuple  of  same  elements  (Strange)
print(b) #   (10 , 20 , 15 , 18)
print(id(b))  # Address  of  new  tuple  (10 , 20 , 15 ,  18)  i.e.  A  different  address
print(type(b))  #  <class  'tuple'>
print(a  is   b)  # False  :  References  'a'  and  'b'  point  to  different  tuples
print(a   ==   b) #  True :  Tuples  'a'  and  'b'  have  same  elements


'''
Which  of  the  following  is  shallow  clone(Assume  that  'a'  is  tuple) ?
1) b = a[:]   --->  Shallow  clone
                          i.e.  Ref  'b'  points  to  same  tuple  where  'a'  points

2) b = tuple(a) ---> Shallow  clone  becoz  tuple  'a'  is  converted  to  same  tuple

3) b = a  ---> Shallow  clone

4) b = tuple(list(a))  --->  Deep  clone
                                       i.e.  Elements  of  tuple  'a'  are  copied  to  tuple  'b'

5) b = (*a,)  --->  Deep  clone
                           i.e.  Elements  of  tuple  'a'  are  copied  to  tuple  'b'

6) b = (*a)  --->  Error  becoz  comma  is  missing

7) b = a . copy()  --->  Error  becoz  tuple  does  not  have  copy()  method 
'''
