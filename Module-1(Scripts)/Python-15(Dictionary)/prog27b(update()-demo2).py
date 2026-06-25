# Find outputs (Home  work)
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b . update(a)  #  Appends  elements  of  tuples  in  list  'a'  to  dict  'b'  in  the  form  of  key : value  pairs
print(b) # {'Y' : 'Yellow' , 'G' : 'Gray' , 'R' : 'Red' , 'B' : 'Blue}
#a . update(b) # Error :  List  does  not  have  update()  method
