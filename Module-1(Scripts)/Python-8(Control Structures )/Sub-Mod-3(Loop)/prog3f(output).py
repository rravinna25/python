# Find  outputs  (Home  work)
for  x   in   ():   #  Not  executed  due  to  empty  tuple
        print(x)
for  x   in  []:  #  Not  executed  due  to  empty  list
        print(x)
for  x   in   {}:  #  Not  executed  due  to  empty  dictionary
        print(x)
for  x   in   set():  #  Not  executed  due  to  empty  set
        print(x)
for  x   in   '':  #  Not  executed  due  to  empty  string
        print(x)
for  x  in  range(10 , 10):  #  Not  executed  due  to  empty  range  object
	print(x)
for  x  in   range():  #  Error :  range()  demands  1 , 2  (or)  3  args  but  not  0
	print(x)
for  x  in   (25):  #   Error :  for  loop  can  not  iterate  thru  non-sequence  such  as  int
	print(x)
