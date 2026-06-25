# Find outputs (Home  work)
def  f1():
	a = 40 #  Creates  Lv  with  value  40
	b = 50  #  Creates  Lv  with  value  50
	c = 60 #  Creates  Lv  with  value  60
	print(a , b , c)  #   40 <space> 50 <space> 60  i.e. Local  variables
	dict = globals()  # Returns  a  dictionary  with  all  the  Gv's   i.e.  {'a' :  10 , 'b' : 20 , 'c' : 30}
	print(dict['a'] , dict['b'] , dict['c'])   #  10 <space> 20 <space> 30  i.e.  Global  variables  
	dict['a'] = 100  #  Modifies  Gv  'a'  to  100
	dict['b'] = 200  #  Modifies  Gv  'b'  to  200
	dict['c'] = 300 #  Modifies  Gv  'c'  to  300
#  Local  variables  a , b  and  c  are  lost	
def  f2():
	print(a , b , c) #  100 <space> 200 <space> 300   i.e.  Global  variables  
# End  of  f2  function
a = 10  #  Creates  Gv  with  value  10
b = 20   #  Creates  Gv  with  value  20
c = 30   #  Creates  Gv  with  value  30
f1()
f2()


'''
40  50  60
10  20  30
100  200  300
'''
