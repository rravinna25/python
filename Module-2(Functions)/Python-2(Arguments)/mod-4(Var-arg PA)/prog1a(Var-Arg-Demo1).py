#  Variable  number  of  arguments  demo  program
def   f1(*t): #  't' is  a  tuple  of  args  passed  to  the  function
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  is  passed  to  the  function
f1()   #  Empty  tuple  is  passed  to  the  function
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})  #  #  Tuple  of  3  elements  is  passed  to  the  function
f1('Hyd')  #  Tuple  of  1  element  is  passed  to  the  function
tpl = (100 , 200 , 150)
f1(tpl)  #  Nested  tuple   is  passed  to  the  function
#f1(t = (10 , 20 , 30))   #  Error :  var-arg  parameter  can  not  be  a  keyword  argument



'''
(10 , 20 , 15 , 18)
<class  'tuple'>
4

()
<class 'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100 , 200 , 150),)
<class 'tuple'>
1
'''
