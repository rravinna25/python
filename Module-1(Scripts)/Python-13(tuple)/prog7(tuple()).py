# tuple()  function  demo  program   (Home  work)
a = range(100 , 150 , 10)
b = tuple(a)   # Converts  range  object  to  tuple
print(b) # (100 , 110 , 120 , 130 , 140)
print(type(b)) # <class 'tuple'>
c = [10 , 20 , 15, 18]
d = tuple(c) # converts  list  to  tuple
print(d) # (10 , 20 , 15 , 18)
e = tuple('Vamsi')  # Converts  string   to  tuple
print(e) # ('V' , 'a' , 'm' , 's' , 'i')
#print(tuple(25)) #Error :  Argument  should  be  a  sequence  but  25  is  not  a   sequence
print(tuple()) #  Returns  an  empty  tuple  i.e.  ()


'''
tuple()  function
--------------------
1) What  does  tuple(sequence)  do  ?  --->  Converts  sequence  to  tuple

2) What  does  tuple(No-args)  do  ?  --->  Returns  an  empty  tuple

3) How  many  arguments  can  tuple()  function  take ?  --->  1 (or)  none  but  not  more  than  one

4) Is  tuple(non-sequence)  valid ?  --->  No  becoz  argument  should  be  sequence  only
'''
