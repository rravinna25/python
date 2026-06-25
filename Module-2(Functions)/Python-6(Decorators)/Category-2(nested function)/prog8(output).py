# Find  outputs (Home  work)
def  outer():
	a = 10 #  Lv  of  outer()  function
	b = 20  #  Lv  of  outer()  function
	def   inner():
		nonlocal   a  #  inner  function  uses  Lv  'a'  of  outer()  function
		a = 100  #  Modifies  Lv  of  outer()  function  to  100
		b = 200  #   Creates  Lv  in  inner()  function
		print(a , b)  #  Lv  of  outer()  function  and  Lv  of  inner()  function  i.e.  100  <space>  200
	# Lv  'b'  of  inner  function  is  lost
	print(a , b)  #   Lv's  of  outer  function  :  10  <space>  20
	inner()  #  Executes  inner()  function
	print(a , b)  #   Lv's  of  outer  function  :  100  <space>  20
# Lv's  'a'  and  'b'  of  outer  function  are  lost
outer() #  Executes  outer()  function


'''
10      20
100    200
100    20


1) How  many  LV's  are  in  outer()  function ?  --->  Two

2) How  many  LV's  are  in  inner()  function ?  ---> One  i.e.  'b'
'''
