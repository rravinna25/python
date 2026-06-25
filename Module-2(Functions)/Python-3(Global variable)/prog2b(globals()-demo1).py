# Find  outputs  (Home  work)
def   f1():
	a = 20   #  Creates  LV  with  value  20
	print(a) #  Lv  i.e.  20
	dict = globals() #  Returns  a  dictionary  with  Gv  i.e. {'a' : 11}
	print(dict['a']) #  11 :  Value  of  key  'a'  in  the  dictionary  i.e. Gv  11
	a = 30   #  Modifies  LV  to  30
	dict['a'] = 40   #  Modifies  GV  to  40
#  Lv  'a'  is  lost
a = 10  #  Creates  GV  with  value  10
print(a) #   Gv  i.e. 10
a += 1 #  Increments  Gv  by  1  i.e.  11
f1()
print(a) #  Gv   i.e. 40


'''
10
20
11
40
'''

'''
1) How  to  distinguish  LV  and  GV  when  they  have  got  same  name ?  --->
																		LV  is  used  by  LV  name  and  GV  is  used  by  globals()['GV  name']

2) globals()['a'] =  40
    What  is  modified ?  ---> GV  'a'

3) In  other  words,  modifying  dictionary  is  as  good  as  modifying  global  variable  becoz  they  refer  to  same  variable
'''
