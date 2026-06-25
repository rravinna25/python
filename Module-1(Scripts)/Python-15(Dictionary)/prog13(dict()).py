#  dict()  function  demo program (Home  work))
a = [ (10 , 'Hyd') , (20 , 'Sec') , (15 , 'Cyb') , (20 , 'Pune')]   #  List  of  tuples
b = dict(a) # Converts  list  of  tuples  to  dictionary
print(b) # {10 : 'Hyd' , 20 : 'Pune' , 15 : 'Cyb'}
c = ( ['R' , 'Red'] , ['G' , 'Green'] , ['B' , 'Blue'] , ['G' , 'Gray'])  #  Tuple  of  lists
d = dict(c) # Converts  tuple  of  lists  to  dictionary
print(d) #  {'R' : 'Red' , 'G' : 'Gray' , 'B' : 'Blue'}
e = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
#print(dict(e)) # Error :  Inner  sequence  has  more  than  2  elements  and  hence  can  not  convert  to  dictionary
f = [[10] , [20] , [30]]
#print(dict(f)) # Error :  Inner  sequence  has  less  than  2  elements  and  hence  can  not  convert  to  dictionary
#print(dict([10 , 20])) # Error : Argument  should  be  nested sequence  but  not  a  sequence
g = [[10 , [20 , 30]] , [40 , [50 , 60]] , [70 , [80 , 90]]]
print(dict(g)) # {10 : [20 , 30] , 40 : [50 , 60] , 70 : [80 , 90]}
h = [[[10 , 20] , 30] , [[40 , 50] , 60] , [[70 , 80] , 90]]
#print(dict(h)) # Error :  Key can  not  be  list  as  it  is  mutable 
i = [[(10 , 20) , 30] , [(40 , 50) , 60] , [(70 , 80) , 90]]
print(dict(i)) # {(10 , 20) : 30 , (40 , 50) : 60 , (70 , 80) : 90}


'''
dict()  function
------------------
1) What  is  the  argument  of  dict()  function ?  --->
											Nested  sequence  such  as  list  of  tuples , list  of  lists , tuple  of  tuples , tuple  of  lists,
											set  of  tuples  and  so  on

2) What  does  dict(nested-sequence)  do ?  --->  Converts  nested  sequence  to  dictionary

3) How  many  elements  can  be  in  each  inner  sequence ?  --->  Exactly  two  elements
    What  are  the  two  elements  of   each  inner  sequence ?  ---> key  and   value

4) Is  dict(sequence)  valid ?  --->  No  becoz  function  expects  nested  sequence  but  not  sequence
'''
