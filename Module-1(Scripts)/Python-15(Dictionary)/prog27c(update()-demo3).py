#  Find  outputs  (Home  work)
a = [(10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = { }
#b . update(a) # Error :  Inner sequence  has  more  than  2  elements
print(b) # {}
c = [(10,) , (20,) , (30,)]
#b . update(c)  # Error :  Inner sequence  has  single  element
print(b) # {}


'''
How  many  elements  can  each  inner  sequence  have ?  --->  Exactly  2  elements
'''
