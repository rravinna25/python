# Find  outputs (Home  work)
x = 10 #  Creates  Gv  with  value  10
def   f1():
	print(x)  #  10 : Gv  is printed  becoz  function  does  not  have  Lv  'x'
	print(globals()['x'])  #  10  i.e.  Gv
# end of the function
f1()
