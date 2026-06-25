# Find outputs (Home work)
x = [1 , 2 , 3 , 4]
y = [1 , 2 , 4 , 3]
print(x == y) # False :  3 == 4  is  False
a = (4 , 1 , 3 , 2)
b = (4 , 2 , 3 , 1)
print(a == b)  # False  :  1 == 2  is  False
p = {1 , 2 , 3 , 4}
q = {4 , 1 , 3 , 2}
print(p == q) # True :  Sets  p  and  q  have  same  elements
m = range(5)
n = range(5)
print(m == n) #   True  :  Objects  'm'  and  'n'  have   same  elements


'''
1) What  is  the  key  when  sequences  are  compared  with  ==  operator ?  --->  1st  non-matching  elements

2) What  about  set ?  --->  Elements  but  not  order  becoz  set  is  unordered
'''
