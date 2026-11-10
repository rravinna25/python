# Find  outputs (Home  work)
class   c1:
	def  __del__(self):  #  self  is  the  object  to  be  lost
		print('Destructor')
		global  b  #  Treats  ref  'b'  as  global  to  destructor
		b = self  #  Ref  'b'  points  to  the  object  which  is   to  be  lost
   # Object  'a'  is  not  lost  due  to  global  ref 'b'  to  the object
a = c1()  #   Creates  an  empty  c1  class  object
del  a   #  Executes  destructor  before  object  'a'  is  lost
print('Hello')
# Destructor  is  not  executed  before  object  'b'  is  lost   becoz  it  is  already executed


'''
Destructor
Hello



1) del  a
    Why  is  destructor  executed ? ---> Since  it  deletes  object  'a'

2) When  is  global  ref  'b'  lost ?  --->  Soon  after  program  terminates

3) Why  is  destructor  not  executed  when  ref  'b'  is  lost ?  --->  Since  it  is  already  executed  when   ref  'a'  is  deleted

4) Finally, how  many  times  is  destructor  executed  for  an  object ?  ---> Just  once
'''
