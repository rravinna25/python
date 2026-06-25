'''
Write  a  program  to  determine  gcd  of  all   the  list  elements

			 	  0      1      2     3     4
List  --->   [12 ,  18 ,   9 ,   7  ,   5]

1) What  is  the  result  of  gcd(12 , 18) ?  ---> 6
    What  is  the  result  of  gcd(6 , 9) ?  ---> 3
    What  is  the  result  of  gcd(3 , 7) ?  ---> 1
    What  is  the  result  of  gcd(1 , 5) ?  --->  1

2) In  general,  what  are  the  arguments  of  gcd()  function ?  --->  Result  and  next  element  of  list
'''
import  math
def gcd_elements(a):
    result = a[0]
    for  x  in  a[1:]:
        result = gcd(result , x)
	# End  of  for  loop		
    return result
#  End  of  the  function	
a = eval(input('Enter list : '))
print('Gcd of list : ' , gcd_elements(a))
