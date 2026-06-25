#  Find  outputs  (Home   work)
def   f1():
	x = 10 #  Lv  of  f1()
	def  f2():
		nonlocal   x  #  Function  f2()  uses  Lv  'x'  of  function  f1()
		def  f3():
			nonlocal   x  #  Function  f3()  uses  Lv  'x'  of  function  f1()  becoz  function  f2()  does  not  have  Lv  'x'  
			print(x)  #   Lv  of  function  f1()  i.e.  10
		# Nothing  is  lost  becoz   function  f3()  does  not  have  Lv  
		f3()   #  Executes  function  f3()
	# Nothing  is  lost  becoz   function  f2()  does  not  have  Lv  
	f2()   #  Executes  function   f2()
# Lv  'x'  of  function  f1  is  lost
f1()   #  Executes  function   f1()
