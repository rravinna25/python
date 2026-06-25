#  Find  outputs  (Home  work)
a = [25 , 10.8 , 'Hyd'] #   Ref  'a'  points  to  list  of  3  elements
print(a) #[25 , 10.8 , 'Hyd']
print(id(a)) #  Address of  list  with  3  elements
print(a * 3) #  Repeats  list  thrice  i.e.  [25 , 10.8 ,  'Hyd'  , 25  ,  10.8  ,   'Hyd' ,  25 ,  10.8 ,  'Hyd']
print(a * 2)  #  Repeats  list  twice i.e.  [25 , 10.8 ,  'Hyd'  , 25  ,  10.8  ,   'Hyd']
print(a * 1)  #  Repeats  list  once  i.e.  [25 , 10.8 ,  'Hyd']
print(a * 0)  #  Repeats  list   0  times  i.e.  []
print(a * -1)   #  Repeats  list   -1  times  i.e.  []
#print(a * 4.0) #  Error  due  to  float  operand  4.0
a = a * 3  #   Ref  'a'   is  modified  to   list  of   9  elements
print(a)  #   [25 , 10.8 ,  'Hyd'  , 25  ,  10.8  ,   'Hyd' ,  25 ,  10.8 ,  'Hyd']
print(id(a)) #  Address of  list  with  9  elements
a = [25]  #   Ref  'a'   is  modified  to   list  of    single   element
print(a , id(a))  #   [25]  <space>  Address  of  list  with  single  element
#print(a * a)  #  Error :  operand2  should  be  an  integer  but  not  list



'''
1) What  does  list  *  n  do ? --->  Repeats  elements  of  list  for  'n'  times

2) list * n
    How  many  elements  are  in  the  resultant  list ?  ---> n * len(list)

3) a = [10 , 20 , 30]
    a = a * 2
	What  is  modified  (List  (or)  reference) ?  ---> Reference  but  not  list

4) a = [10 , 20 , 30]
    a = a * 2
	Where  does  ref  'a'  points  to ?  ---> A  new  list  of  6  elements
'''
