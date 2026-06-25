#  Anonymous  object  demo  program
_ = 25 #   Assigns  25  to  nameless  object
print(_) #  25
print(type(_)) # <class 'int'>
a , _ , c = 10 , 20 , 30  #  Multiple  assignment
print(a) #  10
print(_) #  20
print(c) #  30
for  _  in  range(5):
	print(_ , 'Hello')  #  0 <space> Hello  <next  line>  1  <space> Hello  <next  line>  2 <space> Hello  <next  line>  3  <space> Hello  <next  line>  4 <space> Hello  <next  line>

	
'''
1) How  many  nameless  objects  are  in  the  program ?  --->  7
    How  many  are  alive  ?  ---> 1

2) What  about  remaining   6  nameless  objects ?  --->  Dead
'''
