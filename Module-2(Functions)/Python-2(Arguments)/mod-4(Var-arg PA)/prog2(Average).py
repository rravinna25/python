#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function (Home  work)
def  avg(*a):  #  'a'  is  tuple  of  arguments  passed  from  the  function  call
	try:
		return sum(a) / len(a)
	except  ZeroDivisionError:
		return  0
	except   TypeError:
		return   sum(a[0]) / len(a[0])
# End  of  the  function
print(avg(10 , 20 , 15 , 18))  #  Average  of   10 , 20 ,  15  and  18  i.e.  63 /  4 = 15.75
print(avg(25 , 10.8 , True))   #  Average  of  25 , 10.8 ,  True  i.e.  36.8 / 3 = 12.26
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8)) #  Average  of  5  arguments i.e.   14.26
print(avg())  #  Average  of  0  args  i.e. 0
print(avg(25))  #   Average  of   single  argument  i.e.  25 / 1 = 25.0
print(avg(3 + 4j , 5 + 6j))  #   Average  of   two  arguments  i.e. (8 + 10j) / 2 = 4 + 5j
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))  #   Average  of  nested  tuple  i.e. 63 / 4  = 15.75


'''
1) a = (10 , 20 , 15,  18)
    What  is  sum(a)  ? ---> 63
    What  is  len(a) ? ---> 4

2) a = ((10 , 20 , 15,  18) , )
    What  is  sum(a) ? ---> 0 + (10 , 20 , 15 , 18)  throws   TypeError
    What  is  len(a) ? --->  	1

3) a = ((10 , 20 , 15,  18) , )
    What  are  the  two  ways  to  obtain  inner  tuple  from  tuple  'a'  ?  ---> a[0]  and  *a

4) a = ((10 , 20 , 15,  18) , )
    What  is  a[0] ?  ---> (10 , 20 , 15 , 18)
    What  is  sum(a[0]) ? ---> 63
    What  is  len(a[0]) ? ---> 4

5) a = ((10 , 20 , 15,  18) , )
    What  does  *a  do  ?  --->  Unpacks  outer  tuple  to  obtain  inner  tuple  i.e.  (10 , 20 , 15 , 18)
    What  is  sum(*a) ?  --->  63
    What  is  len(*a) ?  ---> 4

6) What  does  0 / 0  do  ?  ---> Throws  ZeroDivisonError
'''
