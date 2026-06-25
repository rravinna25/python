# Find  output(Home  work)
def  fun():
	x = 10 #  Lv  of   fun()  function
	def    gun():
		#x =  x +  20  #  Error  :  Lv  of  gun()  function  is  not  yet  initialized
		print(x)  #  10 : Lv  of  fun()  function  
	# Nothing  is  lost  as  there  is  no  Lv  in  inner  function
	gun()  #  Executes  gun()  function
#  Lv  'x'  of  outer  function  is  lost
fun() #  Executes  fun()  function
