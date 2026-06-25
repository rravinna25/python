#Find  outputs (Home  work)
a = 10  #  Creates  Gv  with  value  10
def   f1():
	b = 40 #  Creates  Lv  with  value  40
	print('a : ' , a)  #  a :   11  i.e. GV
	print('b : ' , b) #  b :   40  i.e. LV
	print('c : ' , c)  #  c :   31  i.e. GV
	print()
# Lv  'b'  is  lost
b = 20  #  Creates  Gv  with  value  20
def    f2():
	a = 50  #  Creates  Lv  with  value  50
	print('a : ' , a)  #  a : 50  i.e. LV
	print('b : ' , b)  #  b : 22  i.e. GV
	print('c : ' , c)  #  c : 32  i.e. GV
# Lv  'a'  is  lost
c = 30  #  Creates  Gv  with  value  30
print('a : ' , a)  #  a : 10  i.e.  GV
print('b : ' , b)   # b : 20   i.e.  GV
print('c : ' , c)   #  c : 30  i.e. GV
print()
a +=  1 # Increments  Gv  by  1  i.e.  a  is  11
b +=  1  # Increments  Gv  by  1  i.e.  b  is  21
c +=  1  # Increments  Gv  by  1  i.e.  c  is  31
f1()
a +=  1  # Increments  Gv  by  1  i.e.  a  is  12
b +=  1  # Increments  Gv  by  1  i.e.  b  is  22
c +=  1  # Increments  Gv  by  1  i.e.  c  is  32
f2()
print('Bye')
#  Gv's   a , b  and  c  are  lost


'''
a :  10
b :  20
c :  30

a :  11
b :  40
c :  31

a :  50
b :  22
c :  32
Bye
'''



'''
1) Which  variable  is  used  when  both  Lv  and  Gv  have  got  same  name ? --->  LV  due  to  higher  priority

2) Which  variable  is  used  when  function  does  not  have  LV ?  ---> GV
'''
