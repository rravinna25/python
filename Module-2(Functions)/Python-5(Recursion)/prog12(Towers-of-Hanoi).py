#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):  #  'n'  is  number  of  disks , p1  is  source  pole , p2  is  intermediate  pole  and  p3  is  target  pole
	if  n > 0:  #  At  least  one  disk:
		toh(n - 1 , p1 , p3  , p2)  #  How  to  move  (n - 1)  disks  from   pole1  to  pole2  with  pole3  as  intermediate
		print(F'{p1}  --->  {p3}')  #   How  to  move  disk  from  pole1  to  pole3
		toh(n - 1 , p2 ,  p1  , p3)   #  How  to  move  (n - 1)  disks  from   pole2  to  pole3  with  pole1  as  intermediate
# End  of  the  function
n = int(input('How many disks ? :   '))
toh(n , 1 , 2 ,  3)  #  How  to  move  'n'  disks  from   pole1  to  pole3  with  pole2  as  intermediate



'''
What  are  1 , 2 , 3  called  ?  --->  Pole  numbers
'''
