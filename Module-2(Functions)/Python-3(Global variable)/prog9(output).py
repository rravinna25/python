#  Find   outputs
def   f1():
	#x = x + 5 # Error :  Lv  'x'  is  used  on  right  side  without  initialization
	pass
# End  of  f1  function
def  f2():
	x = globals()['x'] + 5 #  Creates  a  LV  with  value   15
	print(x) # LV  i.e. 15
# End of f2  function
x = 10  #  Creates  Gv  with  value  10
f1()
f2()
print(x) # GV i.e. 10


'''
15
10
'''
