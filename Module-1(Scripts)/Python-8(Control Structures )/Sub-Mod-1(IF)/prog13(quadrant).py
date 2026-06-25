'''
Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,
4th  quadrant , x - axis , y - axis   or  origin

1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve

2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve

3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve

4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve

5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0

6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero

7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes

8) Hint:  Use  if  ..   elif
'''
try:
	tpl = eval(input("Enter  x  and  y  co-ordinate  in  the  form  of  tuple  :  "))  
	if  tpl[0] > 0 and  tpl[1] > 0:
		print("1st quadrant")
	elif  tpl[0] < 0 and  tpl[1] > 0:
		print("2nd quadrant")
	elif  tpl[0] < 0 and  tpl[1] < 0:
		print("3rd quadrant")
	elif  tpl[0] > 0 and  tpl[1] < 0:
		print("4th quadrant")
	elif  tpl[0]  != 0 and  tpl[1] == 0:
		print("x-axis")
	elif  tpl[0]  == 0 and  tpl[1] != 0:
		print("y-axis")
	else:
		print("Origin")
except:
	print('Input  should  be  a  tuple')
