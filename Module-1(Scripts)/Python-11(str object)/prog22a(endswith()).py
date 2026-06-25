# endswith()  method  demo  progrram (Home  work)
a = 'Hyd is green city'
print(a . endswith('city'))  #  True :  'Hyd is gree city'  ends  with  'city'
print(a . endswith('town'))  #  False :  'Hyd is gree city'  does  not  end  with  'town'
print(a . endswith('green' , 3 , 12))  #  True :  'Hyd is gree city'  ends  with  'green'  between  indexes  3  and  11
print(a . endswith('green' , 3 , 13))  #   False :  'Hyd is gree city'   does  not  end  with  'green'  between  indexes  3  and  12
print(a . endswith(' ' , 3 , 13))  #  True :  'Hyd is gree city'  ends  with  ' '  between  indexes  3  and  12


'''
endswith()  method
----------------------
1) What  does  str1 . endswith(str2)  do ?  --->  Returns  True  when  str1  ends  with  str2  and  False  otherwise

2) What  does  str1 . endswith(str2 , x , y)  do ?  --->  Returns  True  when  str1  ends  with  str2  between  indexes
																				     x   and  (y - 1)  and  False  otherwise
'''
