#  Find  outputs (Home  work)
def  f1():
	return  10
	return  20  #  Skiped  due  to   return
	return  30  #  Skiped  due  to   return
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1()) # 10
print(f1()) # 10
print(f1()) # 10
print()
g = f2()  #  Creates  an  empty  generator  object
print(next(g)) #  Yields  first  element  10
print(next(g)) #  Yields  next  element  20
print(next(g))  #  Yields  next  element  30
print(next(g)) # StopIteration error : Object  'g'  is  fully  iterated



'''
1) Each  function  call  to  f1()  executes  the  function  from  the  begining  till  return  statement

2) First  function  call  to  next(g)  executes  from  the  begining  till   first   yield  and
    subsequent  function  calls  resume  from  where   function  got  paused  and   continues  till  next  yield
'''
