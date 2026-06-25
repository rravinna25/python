#  Find  outputs
a = [[10 , 20 , 15 , 18]]
#print(sum(a)) # Error :  0 + [10,20,15,18]  throws  error
print(sum(a[0]) )#  sum([10 , 20 , 15 , 18])  is  63
print(sum(*a))  #  sum([10 , 20 , 15 , 18])  is  63


'''
1) a = [[10 , 20 , 15 , 18]]
    What  are  the  two  ways  to  obtain  inner  list ?  ---> a[0]   and  *a

2) What  does  *a  do ?  ---> Unpacks  list  'a'  to  obtain  inner  list
'''
