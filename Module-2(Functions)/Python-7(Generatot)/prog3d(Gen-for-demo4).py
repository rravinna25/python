# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()  #  Creates  1st  generator  object
print(next(g))  #  1st  element  of   1st  genetaor  object  i.e.  25
for  x  in   g:   #  'x'  is  each  element  yielded  of  1st  gen  object  'g'  from  2nd  element
	print(x)    #  10.8  <next line>   Hyd  <next line>
print()
for  x  in   f1():  #  Creates  2nd  generator  object  which  is  iterated  with  for  loop  and  'x'  is  each  element  of  2nd   generator  object  from  1st   element
	print(x)   #  25  <next line>   10.8  <next line>  Hyd  <next line>
print()
gen = f1() #  Creates  3rd  gen  object
print(next(gen))  #  1st  element  of  3rd  gen  object  i.e.  25
for  x  in   f1():  #  Creates  4th  gen  object  which  is  iterated  with  for  loop  and  'x'  is  each  element  of  4th   gen  object  from  1st   element
	print(x)     #  25  <next line>   10.8  <next line>  Hyd  <next line>
print(next(gen))  #  2nd  element  of  3rd  gen  object  i.e.  10.8


'''
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8


1) How  many  generator  objects  are  in  the  above  program ?  ---> Four

2) Which  objects  are  fully  iterated ?  --->  1st , 2nd  and  4th  objects

3) How  many  elements  are  remainging  in  3rd  object ?  --->  Only  one  i.e.  Hyd
'''
